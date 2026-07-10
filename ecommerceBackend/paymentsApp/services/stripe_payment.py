import stripe
from dotenv import load_dotenv
import os
from django.conf import settings
from .payment_strategy import PaymentStrategy
from paymentsApp.models import Payment

from productsApp.models import Product
from cartApp.models import Cart
from django.db import transaction

load_dotenv()


stripe.api_key = os.getenv('STRIPE_SECRET_KEY', getattr(settings, 'STRIPE_SECRET_KEY', None))

class StripePaymentStrategy(PaymentStrategy):
    def create_payment(self, order):
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='payment',
            line_items=[
                {
                    'price_data':{
                        'currency':'usd',
                        'product_data':{
                            'name':f'order #{order.id}'
                        },
                        'unit_amount':int(order.total_price * 100),
                    },
                    'quantity':1,
                }
            ],
            success_url=f'{settings.DOMAIN}/payments/success/?session_id={{CHECKOUT_SESSION_ID}}',
            cancel_url=f'{settings.DOMAIN}/payments/cancel/'
        )

        payment = Payment.objects.create(
            order = order,
            provider = Payment.Provider.STRIPE,
            transaction_id = session.id,
            amount = order.total_price,
            status = Payment.Status.PENDING,
        )

        return {
            'checkout_url':session.url,
            'payment':payment
        }
    
    @transaction.atomic
    def verify_payment(self, payment):
        session = stripe.checkout.Session.retrieve(
            payment.transaction_id
        )

        if session.payment_status == 'paid':
            payment.status = Payment.Status.SUCCESS
            payment.save()

            order = payment.order
            order.status = order.Status.PAID
            order.save()

            for item in order.orderitems.all():

                product = item.product

                if product.stock < item.quantity:
                    raise Exception(
                        f"{product.name} does not have enough stock."
                    )

                product.stock -= item.quantity

                if product.stock == 0:
                    product.featured = False

                product.save()

            try:
                cart = Cart.objects.get(user=order.user)
                cart.cartitems.all().delete()
            except Cart.DoesNotExist:
                pass

            return True
        
        payment.status = Payment.Status.FAILED
        payment.save()

        return False