from .stripe_payment import StripePaymentStrategy
from .bkash_payment import BkashPaymentStrategy


class PaymentFactory:

    @staticmethod
    def get_payment_strategy(provider):

        if provider == "stripe":
            return StripePaymentStrategy()

        elif provider == "bkash":
            return BkashPaymentStrategy()

        raise ValueError("Invalid payment provider.")