# System Architecture

## Overview

This project is a Django REST Framework ecommerce backend with the following components:

- Client: any frontend or external consumer of REST APIs.
- API Layer: Django views and DRF serializers.
- Authentication: JWT authentication using `rest_framework_simplejwt`.
- Business Logic: app-specific services and view logic.
- Database: relational database through Django ORM (SQLite by default, PostgreSQL configured for Docker).
- Cache: local in-memory cache in settings; Redis is referenced but not enabled.
- Payment Providers: Stripe implemented, bKash placeholder exists.
- Deployment: Docker + Docker Compose.

## Architecture Diagram

```mermaid
flowchart TD
    Client[Client / Frontend]
    API[API Layer (Django REST Framework)]
    Auth[Authentication (JWT)]
    Business[Business Logic]
    Database[Database]
    Cache[Cache Layer]
    Payments[Payment Providers]
    External[External Services]
    Docker[Docker / Compose]

    Client --> API
    API --> Auth
    API --> Business
    Business --> Database
    Business --> Cache
    Business --> Payments
    Payments --> External
    API --> Docker
    Database --> Docker
    Cache --> Docker
```

## Components

### Client

- Any frontend or API consumer.
- Uses HTTP to call endpoints under `/api/user/`, `/products/`, `/category/`, `/orders/`, etc.

### API Layer

- Central routing in `ecommerceBackend/config/urls.py`.
- Endpoints distributed across apps: `accountApp`, `productsApp`, `categoriesApp`, `cartApp`, `ordersApp`, `paymentsApp`.
- Uses DRF generic views and APIView classes.

### Authentication

- Custom user model in `accountApp.models.CustomUser`.
- JWT authentication via `rest_framework_simplejwt`.
- Endpoints for login and token refresh.
- Protected views use `IsAuthenticated` from DRF.

### Business Logic

- `accountApp` handles user registration, login, profile, password change, and password reset email flow.
- `productsApp` handles product list, detail, create, update, delete with admin permission.
- `categoriesApp` handles category list, detail, and products under a category.
- `cartApp` handles cart creation and item management.
- `ordersApp` handles checkout, order listing, detail retrieval, and cancellation.
- `paymentsApp` handles Stripe success/cancel callbacks and webhooks.

### Database

- `CustomUser`, `Category`, `Product`, `Cart`, `CartItems`, `Order`, `OrderItem`, and `Payment` are persisted in the database.
- Default database is SQLite under `ecommerceBackend/db.sqlite3`.
- Docker Compose config uses PostgreSQL.

### Cache

- Settings use local memory cache (`LocMemCache`).
- No Redis backend is enabled in `config/settings.py`.

### Payment Providers

- Stripe is implemented using `paymentsApp.services.stripe_payment.StripePaymentStrategy`.
- bKash strategy exists as a placeholder with `NotImplementedError`.

### Docker

- `Dockerfile` builds a Python image, installs packages, copies project code, and collects static files.
- `docker-compose.yml` defines `web` and `db` services.
- Local `.env` file contains environment variables.

## Notes

- Static asset handling is configured through WhiteNoise.
- Payment `stripe` integration is active; `bkash` is not implemented.
- Redis is referenced in `.env` but not enabled in Django settings.
