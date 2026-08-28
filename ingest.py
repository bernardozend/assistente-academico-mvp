from pathlib import Path
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

ARQUIVO = Path("documentos/regulamento_academico_simulado.txt")
BANCO = "banco/chroma"

# Modelo de embeddings multilíngue
embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

# Banco vetorial local
client = chromadb.PersistentClient(path=BANCO)

# Recria a coleção para evitar duplicações durante os testes
try:
    client.delete_collection("documentos_academicos")
except Exception:
    pass

collection = client.create_collection(
    name="documentos_academicos",
    embedding_function=embedding_function
)

texto = ARQUIVO.read_text(encoding="utf-8")

# Divide o documento por seções/parágrafos
trechos = [
    trecho.strip()
    for trecho in texto.split("\n\n")
    if trecho.strip()
]

for i, trecho in enumerate(trechos):
    collection.add(
        ids=[f"trecho_{i}"],
        documents=[trecho],
        metadatas=[
            {
                "arquivo": ARQUIVO.name,
                "trecho": i
            }
        ]
    )

print(f"✅ Documento processado.")
print(f"✅ {len(trechos)} trechos adicionados ao banco vetorial.")
print(f"✅ Banco salvo em: {BANCO}")