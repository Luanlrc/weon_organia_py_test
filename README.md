# 🧠 Weon Organia - API de Classificação de Avaliações

Este projeto é uma API REST construída com **FastAPI** que classifica automaticamente avaliações de clientes como **positiva**, **negativa** ou **neutra** usando **OpenAI**. Os dados são armazenados em um banco **PostgreSQL** e a aplicação está dockerizada para facilitar o uso.

---

## 🚀 Funcionalidades

- 🔍 Classificação de sentimento de avaliações de clientes.
- 📋 Listagem de todas as avaliações.
- 📌 Consulta de avaliação por ID.
- 📊 Geração de relatório por período (com contagem por tipo).
- ❤️ Análise via OpenAI integrada.

---

## 📦 Requisitos

- Docker e Docker Compose instalados

---

## ⚙️ Como rodar

### 1. Clone o repositório
```bash
git clone https://github.com/Luanlrc/weon_organia_py_test.git
cd weon_organia_py_test

weon_organia_py_test/
├── app/
│   ├── agents/
│   │   ├── agents_config.py
│   │   └── sentiment_agent.py
│   ├── api/
│   │   ├── health_check/
│   │   │   ├── models.py
│   │   │   └── routs.py
│   │   ├── routs_reviews/
│   │   │   ├── controllers.py
│   │   │   ├── models.py
│   │   │   └── routs.py
│   │   └── tests/
│   │       ├── test_agent.py
│   │       └── test_reviews.py
│   ├── clients/
│   │   └── database_client.py
│   ├── handlers/
│   │   ├── database_handler.py
│   │   └── llm_handler.py
│   ├── sql/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── config.py
│   ├── main.py
│   └── openai_config.py
├── .env                # não versionado (listado no .gitignore)
├── .local.env          # modelo de variáveis para desenvolvimento
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

### 2. Crie e configure o arquivo .env
Utilize o modelo `.local.env`  
Edite o `.env` com sua chave da OpenAI

### 3. Suba os serviços com Docker Compose
docker compose up --build

### 4. Reiniciar containers (se necessário)
docker compose restart

### 5. Adicionou nova biblioteca no requirements.txt?
docker compose build --no-cache
docker compose up -d   # -d para rodar em segundo plano

### 6. Quer limpar completamente o banco?
Como o banco usa volume persistente, para resetar tudo:
docker compose down -v