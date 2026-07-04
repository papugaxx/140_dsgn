from django.conf import settings
from django.db import models
from django.urls import reverse

from services.models import Service


class Order(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новый'
        REVIEW = 'review', 'На рассмотрении'
        ACCEPTED = 'accepted', 'Принят'
        WAITING_PAYMENT = 'waiting_payment', 'Ожидает оплаты'
        IN_PROGRESS = 'in_progress', 'В работе'
        DONE = 'done', 'Готов'
        REJECTED = 'rejected', 'Отклонён'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name='Клиент')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='orders', verbose_name='Услуга')
    title = models.CharField('Название заказа', max_length=160)
    description = models.TextField('Техническое задание')
    contact = models.CharField('Контакт для связи', max_length=160, blank=True, help_text='Telegram, телефон или email')
    status = models.CharField('Статус', max_length=32, choices=Status.choices, default=Status.NEW)
    price = models.PositiveIntegerField('Цена, грн', blank=True, null=True)
    deadline = models.DateField('Дедлайн', blank=True, null=True)
    admin_comment = models.TextField('Комментарий администратора', blank=True)
    final_file = models.FileField('Финальный файл', upload_to='orders/final/', blank=True, null=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлён', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Заказ #{self.id} — {self.title}'

    def get_absolute_url(self):
        return reverse('orders:detail', kwargs={'pk': self.pk})


class OrderFile(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='files', verbose_name='Заказ')
    file = models.FileField('Файл', upload_to='orders/materials/')
    uploaded_at = models.DateTimeField('Загружен', auto_now_add=True)

    class Meta:
        verbose_name = 'Файл заказа'
        verbose_name_plural = 'Файлы заказа'
        ordering = ['uploaded_at']

    def __str__(self):
        return f'Файл для заказа #{self.order_id}'

    @property
    def filename(self):
        return self.file.name.split('/')[-1]