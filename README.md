# weon_organia_py_test
Desenvolver uma API REST em Python para classificar automaticamente as avaliações de clientes sobre o serviço/produto/suporte de uma empresa em Positiva, Negativa ou Neutra. A API receberá textos de avaliações e retornará a classificação com base em uma análise de sentimento.

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
