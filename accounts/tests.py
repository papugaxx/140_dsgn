from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AccountTests(TestCase):
    def test_register_page_opens(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)

    def test_user_can_register(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'client',
            'first_name': 'Client',
            'email': 'client@example.com',
            'password1': 'TestPass2026!',
            'password2': 'TestPass2026!',
        })

        User = get_user_model()
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='client').exists())