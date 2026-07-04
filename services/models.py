from django.db import models
from django.urls import reverse


class Service(models.Model):
    title = models.CharField('Название', max_length=120)
    slug = models.SlugField('URL-адрес', unique=True)
    short_description = models.CharField('Короткое описание', max_length=220)
    description = models.TextField('Полное описание')
    price_from = models.PositiveIntegerField('Цена от, грн', default=0)
    delivery_time = models.CharField('Срок выполнения', max_length=80, default='2–5 дней')
    image = models.ImageField('Изображение', upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField('Активна', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})