# Introdução

Esse é uma mini aplicação de controle de estoque.

# Objetivo

* Relembrar o conhecimento de Django e Python.

* Ocupar a mente durante a quarentena do COVID-19.

# Projeto base:

* Github: [rg3915/estoque](https://github.com/rg3915/estoque)
* Youtube: [Regis do Python - Controle de Estoque](https://www.youtube.com/playlist?list=PLsGCdfxkV9uqj9DwI6Y72JyvXeA-9mAjc)

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

# Apps no Projeto

## 1. Core

Conteúdo generico para todo o projeto.

### Modelo:

* TimeStampedModel:

- created;
- modified;

## 2. Produto

Controle de produtos.

### Modelo:

* Produto:

- importado;
- ncm;
- produto;
- preco;
- estoque;
- estoque_minimo;

## 3. Estoque

Controle de estoque.

### Modelo:

* Estoque:

- funcionario;
- nf;
- movimento;

* Estoque Itens:

- estoque;
- produto;
- quantidade;
- saldo;

# Links

* [python-decouple](https://github.com/henriquebastos/python-decouple)
* [How to Use Python Decouple](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)
* [Django Basic](https://github.com/rg3915/tutoriais/tree/master/django-basic)
* [Bootstrap Template](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)
* [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks)

