from .payment_strategy import PaymentStrategy

class BkashPaymentStrategy(PaymentStrategy):

    def create_payment(self, order):
        raise NotImplementedError(
            "bKash payment integration is not implemented yet."
        )

    def verify_payment(self, payment):
        raise NotImplementedError(
            "bKash payment verification is not implemented yet."
        )