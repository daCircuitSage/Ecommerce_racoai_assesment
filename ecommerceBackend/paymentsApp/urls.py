from django.urls import path
from .views import (
    PaymentSuccessView,
    PaymentCancelView,
    StripeWebhookView,
)

urlpatterns = [
    path(
        "payments/success/",
        PaymentSuccessView.as_view(),
        name="payment_success",
    ),
    path(
        "payments/cancel/",
        PaymentCancelView.as_view(),
        name="payment_cancel",
    ),
    path(
        "payments/webhook/",
        StripeWebhookView.as_view(),
        name="stripe_webhook",
    ),
]
