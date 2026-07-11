# Environment Configuration Guide

## Purpose

This guide shows how to configure the environment for local development and Docker deployment.

## Required Files

- `.env` — holds sensitive settings and environment-specific values.
- `docker-compose.yml` — uses the `.env` values for the Docker container.

## Recommended `.env` values

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_FROM=your-email@example.com
DOMAIN=http://localhost:8000
NGROK_HOST=
```

## Key Environment Variables

- `SECRET_KEY`
  - Required by Django.
  - Must remain secret in production.

- `DEBUG`
  - Set to `True` for local development.
  - Set to `False` for production.

- `ALLOWED_HOSTS`
  - Comma-separated list of hostnames or IPs that Django will accept.
  - Add ngrok hostnames here when using ngrok.

- Database variables
  - `DB_ENGINE`: `django.db.backends.sqlite3` or `django.db.backends.postgresql`
  - `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`

- Stripe variables
  - `STRIPE_SECRET_KEY` and `STRIPE_PUBLIC_KEY` for Stripe integration.
  - `STRIPE_WEBHOOK_SECRET` for validating webhook requests.

- Email settings
  - `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_FROM` for password reset emails.

- `NGROK_HOST`
  - Optional hostname assigned by ngrok.
  - When set, the project will add it automatically to `ALLOWED_HOSTS` and `CORS_ALLOWED_ORIGINS`.

## Local Development vs Docker

### Local development

The default configuration uses SQLite for local development.
- `DB_ENGINE=django.db.backends.sqlite3`
- `DB_NAME=db.sqlite3`

### Docker / PostgreSQL

When running with Docker Compose, use PostgreSQL settings:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=ecommerce_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

Docker Compose will mount the database volume and connect the `web` service to the `db` service.

## Loading environment variables

The project uses `python-dotenv` and `dotenv.load_dotenv()` in `config/settings.py`, so Django automatically loads `.env` values when the app starts.

## Security

- Do not commit the `.env` file to source control.
- Use separate `.env` files for development and production.
- Keep the `SECRET_KEY` and Stripe keys secret.
