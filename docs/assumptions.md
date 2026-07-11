# Assumptions

## Business Rules

- The application is a backend API only. No frontend is included.
- Users can register, authenticate, manage their profile, and place orders.
- Orders are tied to users and may be paid via Stripe.
- Product inventory is represented with `quantity` in `Product`.

## Model Assumptions

- Categories are flat with no parent-child relations in the current schema.
- Products belong to a single category.
- `Order.status` values include `PENDING`, `PAID`, `FAILED`, etc.
- `Payment.status` includes `pending`, `success`, and `failed`.

## Feature Assumptions

- Stripe payment integration is the only supported provider.
- bKash support is planned but not implemented.
- JWT tokens are used for authentication and authorization.
- Admin users can manage products.

## Deployment

- Docker is the recommended deployment mechanism.
- PostgreSQL is the intended production database.
- SQLite is preserved for local development/testing.

## Testing

- Tests use Django's built-in framework.
- App-level tests are grouped under `*_app/tests/` packages.
- Some `tests.py` modules were removed to avoid dispatch conflicts.
