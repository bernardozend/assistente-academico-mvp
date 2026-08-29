import chromadb
import ollama
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

BANCO = "banco/chroma"
MODELO = "llama3.2:3b"

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

client = chromadb.PersistentClient(path=BANCO)

collection = client.get_collection(
    name="documentos_academicos",
    embedding_function=embedding_function
)


def responder(pergunta):

    resultado = collection.query(
        query_texts=[pergunta],
        n_results=3
    )

    trechos = resultado["documents"][0]
    metadatas = resultado["metadatas"][0]

    contexto_partes = []

    evidencias = []

    for trecho, metadata in zip(trechos, metadatas):

        arquivo = metadata["arquivo"]
        pagina = metadata.get("pagina", 0)

        contexto_partes.append(
            f"""
DOCUMENTO: {arquivo}
PÁGINA: {pagina}

{trecho}
"""
        )

        evidencias.append({
            "arquivo": arquivo,
            "pagina": pagina,
            "trecho": trecho
        })

    contexto = "\n\n".join(contexto_partes)

    prompt = f"""
Você é um assistente acadêmico experimental.

REGRAS OBRIGATÓRIAS:

1. Responda somente utilizando o contexto fornecido.
2. Não utilize conhecimento externo.
3. Não invente informações.
4. Se não houver informação suficiente no contexto,
responda exatamente:

"Não encontrei essa informação na documentação disponível."

5. Responda em português brasileiro.
6. Seja claro e objetivo.
7. Não mencione informações que não estejam presentes nos documentos.

CONTEXTO:

{contexto}

PERGUNTA:

{pergunta}
"""

    resposta = ollama.chat(
        model=MODELO,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta["message"]["content"], evidencias