#Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/WallasDeLis/eventex.svg?branch=master)](https://travis-ci.org/WallasDeLis/eventex)
[![Code Health](https://landscape.io/github/WallasDeLis/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/WallasDeLis/eventex/master)

## Como desenvolver?

1. Clone o repositorio.
2. Crie um virtualenv com python 3.5.
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Execute os teste.

```console
git clone git@github.com:delis/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instancia no heroku.
2. Envie as configurações para o heroku.
3. Define um SECRET_KEY segura para instancia.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o codigo para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force

```