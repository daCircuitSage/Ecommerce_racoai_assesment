# Payment Flow

## Overview

Payment processing is handled by `paymentsApp` with a strategy pattern.
- Stripe is implemented.
- bKash exists as a placeholder with `NotImplementedError`.

## Stripe Payment Flow

```mermaid
sequenceDiagram
    participant Client
    participant API as Django API
    participant OrderService as Order Service
    participant PaymentStrategy as Payment Strategy
    participant Stripe as Stripe API
    participant Webhook as Webhook Endpoint

    Client->>API: POST /orders/checkout/ { provider: "stripe" }
    API->>OrderService: Validate cart, create Order
    OrderService->>PaymentStrategy: get_payment_strategy("stripe")
    PaymentStrategy->>Stripe: checkout.Session.create(...)
    Stripe-->>PaymentStrategy: session object
    PaymentStrategy->>API: return checkout_url
    API-->>Client: 200 { checkout_url }
    Client->>Stripe: Complete payment flow
    Stripe->>API: GET /payments/success/?session_id=<id>
    API->>PaymentStrategy: verify_payment(payment)
    PaymentStrategy->>Stripe: checkout.Session.retrieve(session_id)
    Stripe-->>PaymentStrategy: session status
    PaymentStrategy->>API: return true/false
    API-->>Client: 200 or 400
```

### Data Stored
- `Payment.transaction_id` stores `session.id` from Stripe.
- `Payment.status` stores `pending`, `success`, or `failed`.
- `Order.status` is updated to `PAID` when verification succeeds.

## bKash Payment Flow

bKash is not implemented.
- `paymentsApp.services.bkash_payment.BkashPaymentStrategy.create_payment` raises `NotImplementedError`.
- `paymentsApp.services.bkash_payment.BkashPaymentStrategy.verify_payment` raises `NotImplementedError`.

## Notes
- Stripe flow depends on valid Stripe API keys in environment variables.
- `STRIPE_WEBHOOK_SECRET` is configured but webhook verification currently accepts raw payload when secret is absent.
