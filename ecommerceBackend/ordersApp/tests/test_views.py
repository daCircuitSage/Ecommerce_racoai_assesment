from django.urls import reverse
from rest_framework.test import APITestCase
from accountApp.models import User
from categoriesApp.models import Category
from productsApp.models import Product
from cartApp.models import Cart
from ordersApp.models import Order


class OrderTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='order@example.com', name='Order User', password='TestPass123')
        self.client.force_authenticate(user=self.user)
        category = Category.objects.create(name='Gadgets')
        self.product = Product.objects.create(
            name='Gadget',
            description='Cool gadget',
            price=50.00,
            stock=5,
            category=category
        )
        self.cart = Cart.objects.create(user=self.user)
        self.cart.cartitems.create(product=self.product, quantity=1)

    def test_checkout_empty_provider(self):
        url = reverse('checkout')
        response = self.client.post(url, {'provider': ''})
        self.assertEqual(response.status_code, 400)
        self.assertIn('payment provider is required', response.data['message'])

    def test_order_list_empty(self):
        url = reverse('all_orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
