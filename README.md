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
git clone https://github.com/seuusuario/weon_organia_py_test.git
cd weon_organia_py_test


WEON_ORGANIA_PY_TEST/
├── app/
│   ├── agents/
│   │   └── agents_config.py 
│   ├── api/
│   │   └── routs_reviews/  
│   │       ├── controllers.py
│   │       ├── models.py
│   │       └── routs.py
│   ├── clients/
│   │   └── database_client.py
│   ├── handlers/
│   │   ├── database_handler.py
│   │   └── llm_handler.py
│   ├── sql/
│   │   └── config.py
│   ├── config.py
│   └── main.py
├── tests/
│   └──test_reviews.py 
├── requirements.txt
├── README.md
└── .env
