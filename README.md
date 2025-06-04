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

## 🔐 Segurança e Proteções

Durante o desenvolvimento, consideramos boas práticas de exposição de APIs em ambientes públicos. APIs FastAPI por padrão expõem automaticamente a documentação interativa (`/docs`, `/redoc`) e o arquivo `openapi.json`, que pode ser facilmente explorado por robôs automatizados que mapeiam endpoints e interagem com eles.

Para mitigar esse risco, foram adotadas as seguintes estratégias:

- 🔒 **Autenticação básica** foi adicionada nas rotas de documentação (`/api/docs`, `/api/redoc`, `/api/openapi.json`), impedindo acesso não autorizado aos contratos da API.
- 🛡️ **Rotas padrão foram desabilitadas** (`/docs`, `/redoc`, `/openapi.json`) e substituídas por rotas com prefixo `/api/` para evitar exposição direta.
- 🔑 **Autenticação por token Bearer fixo** foi adicionada como camada extra de segurança para proteção de endpoints sensíveis.

Essas medidas protegem o serviço contra escaneamentos automatizados, reduzem a superfície de ataque e garantem que apenas usuários com conhecimento prévio e autorização possam visualizar e interagir com os recursos da API de maneira controlada.

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