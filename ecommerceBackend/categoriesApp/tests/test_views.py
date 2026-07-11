from django.urls import reverse
from rest_framework.test import APITestCase
from categoriesApp.models import Category
from productsApp.models import Product


class CategoryTests(APITestCase):
    def test_category_list(self):
        Category.objects.create(name='Electronics')
        url = reverse('category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_category_detail(self):
        category = Category.objects.create(name='Books')
        url = reverse('category_detail', kwargs={'slug': category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['slug'], category.slug)

    def test_category_products(self):
        category = Category.objects.create(name='Books')
        Product.objects.create(
            name='Novel',
            description='A great novel',
            price=15.99,
            stock=5,
            category=category
        )
        url = reverse('category_products', kwargs={'slug': category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
