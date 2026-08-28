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
    # Busca os trechos mais relacionados
    resultado = collection.query(
        query_texts=[pergunta],
        n_results=2
    )

    trechos = resultado["documents"][0]
    metadatas = resultado["metadatas"][0]

    contexto = "\n\n".join(
        f"[Fonte: {meta['arquivo']}]\n{trecho}"
        for trecho, meta in zip(trechos, metadatas)
    )

    prompt = f"""
Você é um assistente acadêmico experimental.

REGRAS:
1. Responda SOMENTE com base no contexto fornecido.
2. Não utilize conhecimento externo.
3. Não invente informações.
4. Se o contexto não possuir informação suficiente para responder,
   diga exatamente:
   "Não encontrei essa informação na documentação disponível."
5. Responda em português brasileiro, de forma clara e objetiva.

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

    fontes = list(dict.fromkeys(
        meta["arquivo"] for meta in metadatas
    ))

    return resposta["message"]["content"], fontes


if __name__ == "__main__":
    pergunta = input("Pergunta: ")

    resposta, fontes = responder(pergunta)

    print("\nRESPOSTA:")
    print(resposta)

    print("\nFONTES:")
    for fonte in fontes:
        print(f"- {fonte}")
        