from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('pages', '0001_initial')]

    operations = [
        migrations.AddField('sitesettings', 'meta_description', models.CharField(default='Design Flow — сайт дизайн-студии: услуги, портфолио, личный кабинет и оформление заказов.', max_length=220, verbose_name='SEO-описание')),
        migrations.AddField('sitesettings', 'hero_card_label', models.CharField(default='Пример заказа', max_length=80, verbose_name='Карточка в hero — метка')),
        migrations.AddField('sitesettings', 'hero_card_title', models.CharField(default='Баннер для Telegram', max_length=120, verbose_name='Карточка в hero — заголовок')),
        migrations.AddField('sitesettings', 'hero_card_text', models.TextField(default='Клиент прикрепляет референсы, дизайнер уточняет стоимость, а статус меняется по этапам.', verbose_name='Карточка в hero — текст')),
        migrations.AddField('sitesettings', 'hero_card_price', models.CharField(default='от 700 грн · 1–3 дня', max_length=80, verbose_name='Карточка в hero — цена/срок')),
        migrations.AddField('sitesettings', 'services_kicker', models.CharField(default='Услуги', max_length=80, verbose_name='Блок услуг — метка')),
        migrations.AddField('sitesettings', 'services_title', models.CharField(default='Что можно заказать', max_length=140, verbose_name='Блок услуг — заголовок')),
        migrations.AddField('sitesettings', 'services_text', models.CharField(default='Выбери нужный формат и отправь ТЗ через форму заказа.', max_length=220, verbose_name='Страница услуг — подзаголовок')),
        migrations.AddField('sitesettings', 'portfolio_kicker', models.CharField(default='Портфолио', max_length=80, verbose_name='Блок портфолио — метка')),
        migrations.AddField('sitesettings', 'portfolio_title', models.CharField(default='Работы и кейсы', max_length=140, verbose_name='Блок портфолио — заголовок')),
        migrations.AddField('sitesettings', 'portfolio_text', models.CharField(default='Кейсы, которые показывают стиль и возможности дизайнера.', max_length=220, verbose_name='Страница портфолио — подзаголовок')),
        migrations.AddField('sitesettings', 'cta_label', models.CharField(default='Быстрый старт', max_length=80, verbose_name='CTA — метка')),
        migrations.AddField('sitesettings', 'cta_title', models.CharField(default='Нужен новый дизайн-проект?', max_length=140, verbose_name='CTA — заголовок')),
        migrations.AddField('sitesettings', 'cta_text', models.TextField(default='Создай заказ, прикрепи материалы, а дизайнер оценит срок и стоимость.', verbose_name='CTA — текст')),
        migrations.AddField('sitesettings', 'cta_button_text', models.CharField(default='Создать заказ', max_length=60, verbose_name='CTA — кнопка')),
        migrations.AddField('sitesettings', 'about_feature_services', models.CharField(default='цены, сроки и подробные описания', max_length=180, verbose_name='О проекте — услуги')),
        migrations.AddField('sitesettings', 'about_feature_portfolio', models.CharField(default='категории, кейсы и featured-блок', max_length=180, verbose_name='О проекте — портфолио')),
        migrations.AddField('sitesettings', 'about_feature_orders', models.CharField(default='файлы, статусы, финальный результат', max_length=180, verbose_name='О проекте — заказы')),
        migrations.AddField('sitesettings', 'contacts_title', models.CharField(default='Связь с дизайнером', max_length=140, verbose_name='Контакты — заголовок')),
        migrations.AddField('sitesettings', 'contacts_text', models.TextField(default='Можно написать напрямую, но лучше сразу оформить заказ — так ТЗ и файлы не потеряются.', verbose_name='Контакты — текст')),
    ]
