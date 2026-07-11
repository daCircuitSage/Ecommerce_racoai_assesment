from django.urls import reverse
from rest_framework.test import APITestCase
from accountApp.models import User


class AccountTests(APITestCase):
    def test_register_user(self):
        url = reverse('user-register')
        data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'password': 'TestPass123',
            'password2': 'TestPass123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(email='test@example.com').exists())

    def test_login_user_invalid(self):
        url = reverse('user-login')
        data = {'email': 'noone@example.com', 'password': 'wrongpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 404)
