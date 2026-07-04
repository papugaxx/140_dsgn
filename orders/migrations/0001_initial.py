import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='Название заказа')),
                ('description', models.TextField(verbose_name='Техническое задание')),
                ('contact', models.CharField(blank=True, help_text='Telegram, телефон или email', max_length=160, verbose_name='Контакт для связи')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('review', 'На рассмотрении'), ('accepted', 'Принят'), ('waiting_payment', 'Ожидает оплаты'), ('in_progress', 'В работе'), ('done', 'Готов'), ('rejected', 'Отклонён')], default='new', max_length=32, verbose_name='Статус')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена, грн')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='Дедлайн')),
                ('admin_comment', models.TextField(blank=True, verbose_name='Комментарий администратора')),
                ('final_file', models.FileField(blank=True, null=True, upload_to='orders/final/', verbose_name='Финальный файл')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлён')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='services.service', verbose_name='Услуга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='orders/materials/', verbose_name='Файл')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Загружен')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='orders.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Файл заказа',
                'verbose_name_plural': 'Файлы заказа',
                'ordering': ['uploaded_at'],
            },
        ),
    ]