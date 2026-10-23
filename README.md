# Simple Django Blog

A beginner-friendly Django project with a `post` app and server-rendered pages for reading example posts.

The current post view defines sample post content in Python, so this is a learning project rather than a production publishing platform.

## Run locally

1. Install Python and Django in a virtual environment.
2. From the repository root, run database migrations and start the development server:

```bash
python -m pip install Django
python manage.py migrate
python manage.py runserver
```

Open the local address printed by Django. The project settings module is `storefront.settings`.
