import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

BANCO = "banco/chroma"

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

client = chromadb.PersistentClient(path=BANCO)

collection = client.get_collection(
    name="documentos_academicos",
    embedding_function=embedding_function
)

pergunta = "Como funciona o acesso ao Wi-Fi acadêmico?"

resultado = collection.query(
    query_texts=[pergunta],
    n_results=3
)

print("\nPERGUNTA:")
print(pergunta)

print("\nTRECHOS ENCONTRADOS:\n")

for i, trecho in enumerate(resultado["documents"][0], start=1):

    metadata = resultado["metadatas"][0][i - 1]

    print(f"--- RESULTADO {i} ---")
    print(trecho)

    print(f"\nArquivo: {metadata['arquivo']}")

    if metadata.get("pagina", 0) > 0:
        print(f"Página: {metadata['pagina']}")

    print(f"Trecho: {metadata['trecho']}")
    print()