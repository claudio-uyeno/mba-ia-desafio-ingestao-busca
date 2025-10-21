
# Desafio MBA Engenharia de Software com IA - Full Cycle

Este projeto implementa um sistema de busca semântica e chat sobre documentos PDF, utilizando IA generativa, embeddings e banco de dados vetorial.

## Sumário

- [Visão Geral](#visão-geral)
- [Arquitetura](#arquitetura)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Estrutura dos Arquivos](#estrutura-dos-arquivos)
- [Exemplo de Uso](#exemplo-de-uso)
- [Licença](#licença)

---

## Visão Geral

O sistema permite:
- Ingestão de documentos PDF, extraindo e armazenando embeddings em banco vetorial (Postgres + pgvector).
- Busca semântica sobre o conteúdo do PDF.
- Chat interativo que responde perguntas com base apenas no conteúdo do documento.

## Arquitetura

- **Python**: Scripts principais em `src/`
- **LangChain**: Framework para IA generativa e embeddings
- **Google VertexAI**: Geração de embeddings e modelo de chat
- **Postgres + pgvector**: Armazenamento vetorial
- **Docker Compose**: Banco de dados Postgres configurado com extensão pgvector

## Pré-requisitos

- Python 3.8+
- Docker e Docker Compose
- Conta e credenciais Google VertexAI

## Instalação

1. Clone o repositório:
	```bash
	git clone https://github.com/claudio-uyeno/mba-ia-desafio-ingestao-busca.git
	cd mba-ia-desafio-ingestao-busca
	```

2. Crie e ative o ambiente virtual:
	```bash
	python3 -m venv venv
	source venv/bin/activate
	```

3. Instale as dependências:
	```bash
	pip install -r requirements.txt
	```

4. Suba o banco de dados Postgres com pgvector:
	```bash
	docker-compose up -d
	```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias:

```env
GOOGLE_EMBEDDING_MODEL=vertexai-embedding-model
PG_VECTOR_COLLECTION_NAME=database-collection-name
DATABASE_URL=database-string-connection
LLM_MODEL=vertexai-chat-model
PDF_PATH=full-file-path
```

## Execução

### 1. Ingestão do PDF

Executa a extração e armazenamento dos embeddings do PDF:

```bash
python3 src/ingest.py
```

### 2. Chat de Busca

Inicia o chat interativo:

```bash
python3 src/chat.py
```

Digite sua pergunta e o sistema irá buscar e responder apenas com base no conteúdo do PDF.

## Estrutura dos Arquivos

- `src/ingest.py`: Ingestão do PDF e armazenamento dos embeddings
- `src/search.py`: Busca semântica e montagem do prompt
- `src/chat.py`: Interface de chat interativo
- `document.pdf`: Documento base para busca
- `requirements.txt`: Dependências Python
- `docker-compose.yml`: Banco de dados Postgres com pgvector

## Exemplo de Uso

```
Digite sua pergunta (ou 'sair' para encerrar): qual o ano com maior média de faturamento?
Respota: 
O ano com a maior média de faturamento é 2005, com uma média de R$ 4.356.933.362,66.

Digite sua pergunta (ou 'sair' para encerrar): e qual o pior ano?
Resposta: 
Não tenho informações necessárias para responder sua pergunta.

Digite sua pergunta (ou 'sair' para encerrar): qual a empresa mais nova, mais antiga e seu ano de faturamento?
Resposta:
A empresa mais antiga é Âmbar E-commerce LTDA, fundada em 1930, com faturamento de R$ 33.512.422,19.

As empresas mais novas são:
Pulsar Bebidas ME, fundada em 2023, com faturamento de R$ 61.915.931,36.
Atlas Biotech S.A., fundada em 2023, com faturamento de R$ 9.839.596,80.
```

## Licença

Este projeto é apenas para fins educacionais no MBA Full Cycle.