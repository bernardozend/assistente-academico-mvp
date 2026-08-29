from pathlib import Path
import pymupdf
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

PASTA_DOCUMENTOS = Path("documentos")
BANCO = "banco/chroma"

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

client = chromadb.PersistentClient(path=BANCO)

# Recria a coleção para evitar duplicações
try:
    client.delete_collection("documentos_academicos")
except Exception:
    pass

collection = client.create_collection(
    name="documentos_academicos",
    embedding_function=embedding_function
)


def dividir_texto(texto, tamanho=900, sobreposicao=150):
    texto = " ".join(texto.split())

    if not texto:
        return []

    trechos = []
    inicio = 0

    while inicio < len(texto):
        fim = inicio + tamanho
        trecho = texto[inicio:fim].strip()

        if trecho:
            trechos.append(trecho)

        if fim >= len(texto):
            break

        inicio = fim - sobreposicao

    return trechos


contador = 0
arquivos_processados = 0


# PDFs
for arquivo in PASTA_DOCUMENTOS.glob("*.pdf"):

    print(f"\n📄 Processando PDF: {arquivo.name}")

    pdf = pymupdf.open(arquivo)

    for pagina_numero, pagina in enumerate(pdf, start=1):

        texto = pagina.get_text("text")

        trechos = dividir_texto(texto)

        for trecho_numero, trecho in enumerate(trechos, start=1):

            collection.add(
                ids=[f"trecho_{contador}"],
                documents=[trecho],
                metadatas=[{
                    "arquivo": arquivo.name,
                    "pagina": pagina_numero,
                    "trecho": trecho_numero,
                    "tipo": "PDF"
                }]
            )

            contador += 1

    pdf.close()

    arquivos_processados += 1


# TXT
for arquivo in PASTA_DOCUMENTOS.glob("*.txt"):

    print(f"\n📝 Processando TXT: {arquivo.name}")

    texto = arquivo.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    trechos = dividir_texto(texto)

    for trecho_numero, trecho in enumerate(trechos, start=1):

        collection.add(
            ids=[f"trecho_{contador}"],
            documents=[trecho],
            metadatas=[{
                "arquivo": arquivo.name,
                "pagina": 0,
                "trecho": trecho_numero,
                "tipo": "TXT"
            }]
        )

        contador += 1

    arquivos_processados += 1


print("\n==============================")
print("✅ INDEXAÇÃO FINALIZADA")
print(f"📚 Arquivos processados: {arquivos_processados}")
print(f"🧩 Trechos adicionados: {contador}")
print(f"💾 Banco: {BANCO}")
print("==============================")