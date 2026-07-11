from django.urls import reverse
from rest_framework.test import APITestCase
from accountApp.models import User
from categoriesApp.models import Category
from productsApp.models import Product
from cartApp.models import Cart


class CartTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='cart@example.com', name='Cart User', password='TestPass123')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name='Games')
        self.product = Product.objects.create(
            name='Board Game',
            description='Fun game',
            price=20.00,
            stock=5,
            category=self.category
        )

    def test_add_to_cart(self):
        url = reverse('add_to_cart')
        data = {'product_id': self.product.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Cart.objects.count(), 1)

    def test_update_item_quantity_invalid(self):
        cart = Cart.objects.create(user=self.user)
        cart_item = cart.cartitems.create(product=self.product, quantity=1)
        url = reverse('update_quantity')
        response = self.client.patch(url, {'item_id': cart_item.id, 'quantity': 0}, format='json')
        self.assertEqual(response.status_code, 400)
