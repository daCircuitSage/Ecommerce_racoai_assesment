import json
import os

import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Payment
from .services.stripe_payment import StripePaymentStrategy


class PaymentSuccessView(APIView):
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
            Payment.objects.select_related('order__user'),
            transaction_id=session_id,
            provider=Payment.Provider.STRIPE
        )

        strategy = StripePaymentStrategy()

        if strategy.verify_payment(payment):
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
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        session_id = request.query_params.get("session_id")

        if session_id:
            try:
                payment = Payment.objects.select_related('order').get(transaction_id=session_id)
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


@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
        webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET', getattr(settings, 'STRIPE_WEBHOOK_SECRET', None))

        if webhook_secret:
            try:
                event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
            except ValueError:
                return Response({'message': 'Invalid payload.'}, status=status.HTTP_400_BAD_REQUEST)
            except stripe.error.SignatureVerificationError:
                return Response({'message': 'Invalid signature.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                event = json.loads(payload.decode('utf-8'))
            except json.JSONDecodeError:
                return Response({'message': 'Invalid payload.'}, status=status.HTTP_400_BAD_REQUEST)

        event_type = event.get('type')
        data_object = event.get('data', {}).get('object', {})

        if event_type == 'checkout.session.completed':
            session_id = data_object.get('id')
            if session_id:
                try:
                    payment = Payment.objects.select_related('order').get(transaction_id=session_id)
                    StripePaymentStrategy().verify_payment(payment)
                except Payment.DoesNotExist:
                    pass

        return Response({'status': 'success'}, status=status.HTTP_200_OK)
