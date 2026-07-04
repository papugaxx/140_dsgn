from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='Design Flow', max_length=80, verbose_name='Название сайта')),
                ('logo_text', models.CharField(default='DF', max_length=12, verbose_name='Текст логотипа')),
                ('tagline', models.CharField(default='Студия графического и digital-дизайна', max_length=180, verbose_name='Короткое описание')),
                ('hero_badge', models.CharField(default='Портфолио · услуги · заказы', max_length=120, verbose_name='Бейдж на главной')),
                ('hero_title', models.CharField(default='Дизайн для брендов, соцсетей и digital-проектов', max_length=180, verbose_name='Заголовок главной')),
                ('hero_text', models.TextField(default='Выбираешь услугу, отправляешь ТЗ и материалы, а дальше отслеживаешь статус заказа в личном кабинете.', verbose_name='Текст главной')),
                ('primary_cta_text', models.CharField(default='Оформить заказ', max_length=60, verbose_name='Текст основной кнопки')),
                ('secondary_cta_text', models.CharField(default='Смотреть работы', max_length=60, verbose_name='Текст второй кнопки')),
                ('stat_one_value', models.CharField(default='4+', max_length=24, verbose_name='Статистика 1 — число')),
                ('stat_one_label', models.CharField(default='направления дизайна', max_length=80, verbose_name='Статистика 1 — подпись')),
                ('stat_two_value', models.CharField(default='5', max_length=24, verbose_name='Статистика 2 — число')),
                ('stat_two_label', models.CharField(default='файлов к заказу', max_length=80, verbose_name='Статистика 2 — подпись')),
                ('stat_three_value', models.CharField(default='24/7', max_length=24, verbose_name='Статистика 3 — число')),
                ('stat_three_label', models.CharField(default='доступ к статусам', max_length=80, verbose_name='Статистика 3 — подпись')),
                ('about_title', models.CharField(default='Сайт дизайнера, который выглядит как готовый продукт', max_length=160, verbose_name='Заголовок страницы О проекте')),
                ('about_text', models.TextField(default='Проект помогает дизайнеру не терять заявки в переписках: клиент оформляет заказ через сайт, загружает материалы и видит статус выполнения.', verbose_name='Текст страницы О проекте')),
                ('telegram', models.CharField(default='@designer', max_length=80, verbose_name='Telegram')),
                ('email', models.EmailField(default='hello@designflow.test', max_length=254, verbose_name='Email')),
                ('response_time', models.CharField(default='обычно в течение дня', max_length=100, verbose_name='Время ответа')),
                ('footer_text', models.CharField(default='Студия графического и digital-дизайна.', max_length=180, verbose_name='Текст в футере')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={'verbose_name': 'Настройки сайта', 'verbose_name_plural': 'Настройки сайта'},
        ),
    ]
