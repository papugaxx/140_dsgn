from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL-адрес')),
                ('short_description', models.CharField(max_length=220, verbose_name='Короткое описание')),
                ('description', models.TextField(verbose_name='Полное описание')),
                ('price_from', models.PositiveIntegerField(default=0, verbose_name='Цена от, грн')),
                ('delivery_time', models.CharField(default='2–5 дней', max_length=80, verbose_name='Срок выполнения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ['title'],
            },
        ),
    ]