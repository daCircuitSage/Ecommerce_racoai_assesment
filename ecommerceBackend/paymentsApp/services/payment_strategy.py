from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def create_payment(self, order):
        """
        Creates a payment with the selected provider.
        Returns payment information (e.g. checkout URL).
        """
        pass

    @abstractmethod
    def verify_payment(self, payment):
        """
        Verifies whether the payment was successful.
        Returns True or False.
        """
        pass