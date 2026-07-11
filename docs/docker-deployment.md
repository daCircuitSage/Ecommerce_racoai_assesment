# Docker Deployment

## Docker Components

- `Dockerfile`
- `docker-compose.yml`
- `.dockerignore`
- `.env`

## Dockerfile Behavior

The `Dockerfile`:
- starts from `python:3.13-slim`
- installs dependencies from `requirements.txt`
- copies project files into `/app`
- changes working directory to `/app/ecommerceBackend`
- runs `python manage.py collectstatic --noinput`
- exposes port `8000`
- uses `gunicorn` to serve the app

## Docker Compose

The `docker-compose.yml` defines:
- `web` service for the Django app
- `db` service for PostgreSQL
- volumes for static files and media
- environment variables via `.env`
- `web` depends on `db`

## Startup Flow

1. `docker compose build --no-cache`
2. `docker compose up`
3. Django migrates and starts Gunicorn
4. App available on `http://localhost:8000`

## Environment Variables

Important variables:
- `SECRET_KEY`
- `DEBUG`
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `STRIPE_SECRET_KEY`, `STRIPE_PUBLIC_KEY`, `STRIPE_WEBHOOK_SECRET`
- `DOMAIN`
- Email credentials

## Volumes

- `static_volume` for `staticfiles`
- `media_volume` for user-uploaded media
- `postgres_data` for PostgreSQL persistence

## Notes

- `DEBUG=False` is set in compose environment for `web`.
- `collectstatic` is run during Docker build.
- PostgreSQL is configured in compose, but SQLite is still supported by settings.
