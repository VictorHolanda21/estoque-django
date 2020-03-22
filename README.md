# Introdução

Esse é uma mini aplicação de controle de estoque.

# Objetivo

Relembrar o conhecimento de Django e Python.

# Como rodar o projeto?

* Clone esse repositório
* Crie um virtualenv com Python3
* Ative o virtualenv
* Instale as dependências
* Rode as migrações

# Comandos

```
git clone {URL}
cd estoque
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

