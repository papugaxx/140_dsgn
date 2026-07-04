from django.db import models
from django.urls import reverse


class PortfolioCategory(models.Model):
    name = models.CharField('Название', max_length=80)
    slug = models.SlugField('URL-адрес', unique=True)

    class Meta:
        verbose_name = 'Категория портфолио'
        verbose_name_plural = 'Категории портфолио'
        ordering = ['name']

    def __str__(self):
        return self.name


class PortfolioItem(models.Model):
    title = models.CharField('Название работы', max_length=140)
    slug = models.SlugField('URL-адрес', unique=True)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='items', verbose_name='Категория')
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='portfolio/', blank=True, null=True)
    client = models.CharField('Клиент', max_length=120, blank=True)
    is_featured = models.BooleanField('Показывать на главной', default=False)
    created_at = models.DateField('Дата работы', auto_now_add=True)

    class Meta:
        verbose_name = 'Работа в портфолио'
        verbose_name_plural = 'Работы в портфолио'
        ordering = ['-created_at', '-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:detail', kwargs={'slug': self.slug})