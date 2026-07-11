# Authentication

## JWT Authentication

This project uses JWT authentication powered by `djangorestframework-simplejwt`.

### Token Endpoints

- `POST /api/token/` - obtain access and refresh tokens
- `POST /api/token/refresh/` - obtain a new access token

### Token Configuration

Configured in `config/settings.py`:
- `ACCESS_TOKEN_LIFETIME`: 5 minutes
- `REFRESH_TOKEN_LIFETIME`: 1 day
- `AUTH_HEADER_TYPES`: `Bearer`
- `USER_ID_FIELD`: `id`
- `USER_ID_CLAIM`: `user_id`

## Protected APIs

Views use `IsAuthenticated` for protected endpoints:
- User profile
- Change password
- Cart operations
- Order operations
- Product create/update/delete operations

## Custom User Model

- `accountApp.models.CustomUser`
- Uses email as username field
- `is_admin` indicates staff privileges
- `AUTH_USER_MODEL` is set in `config/settings.py`

## Permissions

- `productsApp.permissions.IsAdminUserOnly` restricts product management to admin users.

## Authorization Flow

1. User registers or logs in.
2. Server returns JWT tokens.
3. Client sends `Authorization: Bearer <access_token>`.
4. Django validates token using Simple JWT.
5. Protected endpoints are allowed based on authentication and permissions.
