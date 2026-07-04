from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL-адрес')),
            ],
            options={
                'verbose_name': 'Категория портфолио',
                'verbose_name_plural': 'Категории портфолио',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Название работы')),
                ('slug', models.SlugField(unique=True, verbose_name='URL-адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio/', verbose_name='Изображение')),
                ('client', models.CharField(blank=True, max_length=120, verbose_name='Клиент')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Показывать на главной')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата работы')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=models.SET_NULL, related_name='items', to='portfolio.portfoliocategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Работа в портфолио',
                'verbose_name_plural': 'Работы в портфолио',
                'ordering': ['-created_at', '-id'],
            },
        ),
    ]