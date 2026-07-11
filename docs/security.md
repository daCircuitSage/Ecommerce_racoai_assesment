# Security

## Secret Management

- Secrets are loaded from environment variables in `config/settings.py`.
- `SECRET_KEY` is required and should not be committed.
- Stripe API keys and email credentials are also pulled from environment variables.

## Production Settings

- `DEBUG` should be `False` in production.
- `ALLOWED_HOSTS` should contain valid hostnames.
- `CSRF_TRUSTED_ORIGINS` should be configured if using cross-origin forms.

## Static File Security

- `Whitenoise` is used to serve static files in production.
- `STATIC_ROOT` and `STATICFILES_DIRS` are configured for collectstatic.

## HTTP Headers

- The current configuration does not show explicit security middleware settings beyond Django defaults.
- For production, add `SecurityMiddleware` and configure:
  - `SECURE_SSL_REDIRECT`
  - `SESSION_COOKIE_SECURE`
  - `CSRF_COOKIE_SECURE`
  - `SECURE_HSTS_SECONDS`

## JWT Security

- Access tokens are short-lived (5 minutes).
- Refresh tokens live 1 day.
- Tokens are sent via `Authorization: Bearer <token>`.

## Notes

- The project uses a custom user model and email-based authentication.
- Password validation is enabled by default through Django settings.
- Email verification is not implemented.
