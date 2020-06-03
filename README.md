# SistemaCadastro
Um simples sistema de cadastro com Python, [MongoDB](https://www.mongodb.com/) e [django](https://www.djangoproject.com/).

# Linux
### Instalação

```shell
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

## Execução

### Produção
```shel
gunicorn --bind 127.0.0.1:8000 sistema.wsgi
```
### Desenvolvimento
```shel
# Lembre-se de definir sistema/settings.py: DEBUG=True
python3 manage.py runserver
```


# Windows
### Instalação

```shel
pip install --upgrade pip setuptools
pip install -r requirements.txt
pip install waitress
```

## Execução

### Produção
```shel
# O gunicorn é exclusivo para Unix, sendo assim, você pode usar o Waitress como substituto
waitress-serve --listen=*:8000 sistema.wsgi:application
```


### Desenvolvimento
```shel
# Lembre-se de definir sistema/settings.py: DEBUG=True
python3 manage.py runserver
```
