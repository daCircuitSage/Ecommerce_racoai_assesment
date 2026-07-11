# Local ngrok Setup Guide

## Purpose

This guide explains how to configure ngrok for local development with the Django ecommerce API.

## Prerequisites

- Django app must be running locally on port `8000`
- ngrok installed and authenticated

## Start the Django app

For local development:
```bash
cd ecommerceBackend
python manage.py runserver 0.0.0.0:8000
```

For Docker:
```bash
docker compose up
```

## Start ngrok

Run in a separate terminal:
```bash
ngrok http 8000
```

This will provide a public URL like:
- `https://elda-craglike-uncolourably.ngrok-free.dev`

## Update `.env`

Add the ngrok host to `.env`:

```env
NGROK_HOST=elda-craglike-uncolourably.ngrok-free.dev
```

If you use a new ngrok URL later, update `NGROK_HOST` accordingly.

## Django settings changes

The project already supports ngrok by reading `NGROK_HOST` in `config/settings.py`.

### What the settings do

- Adds the ngrok hostname to `ALLOWED_HOSTS`
- Adds the ngrok URL to `CORS_ALLOWED_ORIGINS`
- Accepts any free ngrok domain pattern via regex

## Frontend usage

If you access the API through a frontend hosted on ngrok, request URLs should use the public ngrok URL:

```text
https://elda-craglike-uncolourably.ngrok-free.dev/products/
```

## Stripe webhooks

If Stripe is used, configure webhook endpoint in Stripe dashboard to:

```text
https://elda-craglike-uncolourably.ngrok-free.dev/payments/webhook/
```

## Example `.env` for ngrok

```env
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,elda-craglike-uncolourably.ngrok-free.dev
NGROK_HOST=elda-craglike-uncolourably.ngrok-free.dev
```

## Optional ngrok config file

Create `ngrok.yml` in your home directory or repo:

```yaml
authtoken: YOUR_NGROK_AUTH_TOKEN
tunnels:
  django:
    proto: http
    addr: 8000
    host_header: rewrite
```

Then start with:
```bash
ngrok start django
```

## Notes

- When ngrok restarts, the public URL usually changes unless you have a reserved domain.
- Update `NGROK_HOST` whenever the public URL changes.
