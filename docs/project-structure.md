# Project Structure

## Folder Tree

```
DRF_Ecommerce_api/
├── Dockerfile
├── docker-compose.yml
├── .env
├── .dockerignore
├── requirements.txt
├── ecommerceBackend/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── accountApp/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   ├── views.py
│   │   └── tests/
│   ├── categoriesApp/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   ├── views.py
│   │   └── tests/
│   ├── productsApp/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests/
│   ├── cartApp/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests/
│   ├── ordersApp/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests/
│   ├── paymentsApp/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── services/
│   │   │   ├── bkash_payment.py
│   │   │   ├── payment_factory.py
│   │   │   ├── payment_strategy.py
│   │   │   └── stripe_payment.py
│   │   └── tests/
│   ├── media/
│   └── manage.py
└── docs/
    └── ...
```

## App Responsibilities

- `accountApp`
  - Custom user model and authentication-related views.
  - JWT login, registration, password reset, user profile, and password change.

- `categoriesApp`
  - Category CRUD through read-only endpoints.
  - Category detail and category-specific product listing.
  - Uses a simple category descendant helper (`category_descendants`) but current model does not implement parent-child relationships.

- `productsApp`
  - Product listing and detail retrieval.
  - Create, update, delete operations require authenticated admin users.
  - Uses `IsAdminUserOnly` permission.

- `cartApp`
  - Cart ownership and cart item management.
  - Add to cart, update quantity, and delete cart item.

- `ordersApp`
  - Checkout flow and order management.
  - Order list, detail retrieval, and cancel order flow.

- `paymentsApp`
  - Stripe payment flow and webhook handling.
  - Strategy pattern with Stripe and placeholder bKash implementation.

- `config`
  - Django settings, URL routing, WSGI configuration.
  - JWT configuration, static file config, database and email settings.

## Test Structure

- Each app has a `tests/` package for unit tests.
- `tests.py` app-level files were removed to avoid discovery conflicts.

## Not Implemented / Missing

- Category parent-child relationship is referenced in code, but `Category` model has no `parent` field.
- `bkash_payment` integration is explicitly not implemented.
- Redis is not configured in Django settings; cache uses in-memory default.
