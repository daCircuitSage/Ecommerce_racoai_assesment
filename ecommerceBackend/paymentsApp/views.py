from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Payment
from .services.stripe_payment import StripePaymentStrategy


class PaymentSuccessView(APIView):
    # allow Stripe redirect (user agent) to reach this endpoint without token
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        session_id = request.query_params.get("session_id")

        if not session_id:
            return Response(
                {"message": "Session ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        payment = get_object_or_404(
            Payment,
            transaction_id=session_id,
            provider=Payment.Provider.STRIPE
        )

        strategy = StripePaymentStrategy()

        if strategy.verify_payment(payment):
            # clear user's cart after successful payment
            try:
                from cartApp.models import Cart

                cart = Cart.objects.get(user=payment.order.user)
                cart.cartitems.all().delete()
            except Exception:
                pass

            return Response(
                {
                    "message": "Payment successful.",
                    "order_id": payment.order.id,
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "message": "Payment verification failed."
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class PaymentCancelView(APIView):
    # allow Stripe redirect to this endpoint without token
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        session_id = request.query_params.get("session_id")

        if session_id:
            try:
                payment = Payment.objects.get(transaction_id=session_id)
                payment.status = Payment.Status.FAILED
                payment.save()

                order = payment.order
                order.status = order.Status.CANCELLED
                order.save()
            except Payment.DoesNotExist:
                pass

        return Response(
            {
                "message": "Payment was cancelled."
            },
            status=status.HTTP_200_OK
        )