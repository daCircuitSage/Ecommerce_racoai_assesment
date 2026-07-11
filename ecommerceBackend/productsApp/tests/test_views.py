from django.urls import reverse
from rest_framework.test import APITestCase
from productsApp.models import Product
from categoriesApp.models import Category


class ProductTests(APITestCase):
    def test_product_list(self):
        category = Category.objects.create(name='Toys')
        Product.objects.create(
            name='Toy Car',
            description='A toy',
            price=9.99,
            stock=10,
            category=category
        )
        url = reverse('product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_product_detail(self):
        category = Category.objects.create(name='Toys')
        product = Product.objects.create(
            name='Toy Car',
            description='A toy',
            price=9.99,
            stock=10,
            category=category
        )
        url = reverse('product_detail', kwargs={'slug': product.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['slug'], product.slug)
