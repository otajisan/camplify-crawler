# camplify-crawler

- Find a campsite in Japan

# Project making

```bash
pipenv install poetry
pipenv shell

poetry init
poetry add django
poetry run django-admin startproject camplify_crawler .
poetry run ./manage.py startapp crawler
```