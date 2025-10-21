import os
from dotenv import load_dotenv

from langchain_google_vertexai import VertexAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""



def search_prompt(question=None):
    embeddings = VertexAIEmbeddings(
        model_name=os.environ["GOOGLE_EMBEDDING_MODEL"]
    )

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.environ["PG_VECTOR_COLLECTION_NAME"],
        connection=os.environ["DATABASE_URL"],
        use_jsonb=True
    )

    documents = store.similarity_search_with_score(question, k=10)

    if not documents:
      return "Não tenho informações necessárias para responder sua pergunta."
    
    context = "\n\n".join([doc.page_content for doc, _ in documents])

    prompt = PROMPT_TEMPLATE.format(contexto=context, pergunta=question)

    message = [
        {"role": "user", "content": prompt}
    ]

    return message
