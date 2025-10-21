import os
from dotenv import load_dotenv
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_postgres import PGVector

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")

def ingest_pdf():
    if not PDF_PATH:
        raise RuntimeError(f"Missing required environment variable: PDF_PATH")

    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()
    splits = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150, add_start_index=False).split_documents(documents)

    if not splits:
        raise SystemExit("No document chunks were created from the PDF.")

    enriched = [
        Document(
            page_content=d.page_content,
            metadata={k: v for k, v in d.metadata.items() if v not in ("" , None)}
        )
        for d in splits
    ]

    ids = [f"doc-{i}" for i in range(len(enriched))]

    embeddings = VertexAIEmbeddings(
        model_name=os.environ["GOOGLE_EMBEDDING_MODEL"]
    )

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.environ["PG_VECTOR_COLLECTION_NAME"],
        connection=os.environ["DATABASE_URL"],
        use_jsonb=True
    )

    store.add_documents(documents=enriched, ids=ids)

if __name__ == "__main__":
    ingest_pdf()