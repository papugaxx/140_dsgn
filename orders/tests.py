from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from services.models import Service
from .models import Order


class OrderTests(TestCase):
    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username='client',
            password='ClientPass2026!'
        )

        self.service = Service.objects.create(
            title='Баннер',
            slug='banner',
            short_description='Тест',
            description='Описание услуги',
            price_from=700,
        )

    def test_order_page_requires_login(self):
        response = self.client.get(reverse('orders:create'))
        self.assertEqual(response.status_code, 302)

    def test_user_can_create_order(self):
        self.client.login(username='client', password='ClientPass2026!')

        file = SimpleUploadedFile(
            'brief.pdf',
            b'file content',
            content_type='application/pdf'
        )

        response = self.client.post(reverse('orders:create'), {
            'service': self.service.id,
            'title': 'Новый заказ',
            'description': 'Описание заказа',
            'contact': '@client',
            'files': file,
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Order.objects.filter(title='Новый заказ').exists())

    def test_user_sees_orders_page(self):
        Order.objects.create(
            user=self.user,
            service=self.service,
            title='Тестовый заказ',
            description='Описание',
        )

        self.client.login(username='client', password='ClientPass2026!')

        response = self.client.get(reverse('orders:list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовый заказ')