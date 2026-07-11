from django.urls import reverse
from rest_framework.test import APITestCase
from accountApp.models import User
from categoriesApp.models import Category
from productsApp.models import Product
from ordersApp.models import Order
from paymentsApp.models import Payment


class PaymentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='pay@example.com', name='Pay User', password='TestPass123')
        category = Category.objects.create(name='Gadgets')
        self.product = Product.objects.create(
            name='Gadget',
            description='Cool gadget',
            price=50.00,
            stock=5,
            category=category
        )
        self.order = Order.objects.create(user=self.user, total_price=50.00)
        self.payment = Payment.objects.create(
            order=self.order,
            provider=Payment.Provider.STRIPE,
            transaction_id='test-session',
            amount=50.00,
            status=Payment.Status.PENDING,
        )

    def test_payment_success_missing_session_id(self):
        url = reverse('payment_success')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    def test_payment_cancel_no_session_id(self):
        url = reverse('payment_cancel')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Payment was cancelled.')
