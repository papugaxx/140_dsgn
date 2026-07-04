from django.db import models


class SiteSettings(models.Model):
    """Singleton with all public-facing copy used by the marketing pages."""

    site_name = models.CharField('Название сайта', max_length=80, default='Design Flow')
    logo_text = models.CharField('Текст логотипа', max_length=12, default='DF')
    tagline = models.CharField('Короткое описание', max_length=180, default='Студия графического и digital-дизайна')
    meta_description = models.CharField(
        'SEO-описание',
        max_length=220,
        default='Design Flow — сайт дизайн-студии: услуги, портфолио, личный кабинет и оформление заказов.',
    )

    hero_badge = models.CharField('Бейдж на главной', max_length=120, default='Портфолио · услуги · заказы')
    hero_title = models.CharField('Заголовок главной', max_length=180, default='Дизайн для брендов, соцсетей и digital-проектов')
    hero_text = models.TextField('Текст главной', default='Выбираешь услугу, отправляешь ТЗ и материалы, а дальше отслеживаешь статус заказа в личном кабинете.')
    primary_cta_text = models.CharField('Текст основной кнопки', max_length=60, default='Оформить заказ')
    secondary_cta_text = models.CharField('Текст второй кнопки', max_length=60, default='Смотреть работы')

    hero_card_label = models.CharField('Карточка в hero — метка', max_length=80, default='Пример заказа')
    hero_card_title = models.CharField('Карточка в hero — заголовок', max_length=120, default='Баннер для Telegram')
    hero_card_text = models.TextField('Карточка в hero — текст', default='Клиент прикрепляет референсы, дизайнер уточняет стоимость, а статус меняется по этапам.')
    hero_card_price = models.CharField('Карточка в hero — цена/срок', max_length=80, default='от 700 грн · 1–3 дня')

    stat_one_value = models.CharField('Статистика 1 — число', max_length=24, default='4+')
    stat_one_label = models.CharField('Статистика 1 — подпись', max_length=80, default='направления дизайна')
    stat_two_value = models.CharField('Статистика 2 — число', max_length=24, default='5')
    stat_two_label = models.CharField('Статистика 2 — подпись', max_length=80, default='файлов к заказу')
    stat_three_value = models.CharField('Статистика 3 — число', max_length=24, default='24/7')
    stat_three_label = models.CharField('Статистика 3 — подпись', max_length=80, default='доступ к статусам')

    services_kicker = models.CharField('Блок услуг — метка', max_length=80, default='Услуги')
    services_title = models.CharField('Блок услуг — заголовок', max_length=140, default='Что можно заказать')
    services_text = models.CharField('Страница услуг — подзаголовок', max_length=220, default='Выбери нужный формат и отправь ТЗ через форму заказа.')

    portfolio_kicker = models.CharField('Блок портфолио — метка', max_length=80, default='Портфолио')
    portfolio_title = models.CharField('Блок портфолио — заголовок', max_length=140, default='Работы и кейсы')
    portfolio_text = models.CharField('Страница портфолио — подзаголовок', max_length=220, default='Кейсы, которые показывают стиль и возможности дизайнера.')

    cta_label = models.CharField('CTA — метка', max_length=80, default='Быстрый старт')
    cta_title = models.CharField('CTA — заголовок', max_length=140, default='Нужен новый дизайн-проект?')
    cta_text = models.TextField('CTA — текст', default='Создай заказ, прикрепи материалы, а дизайнер оценит срок и стоимость.')
    cta_button_text = models.CharField('CTA — кнопка', max_length=60, default='Создать заказ')

    about_title = models.CharField('Заголовок страницы О проекте', max_length=160, default='Сайт дизайнера, который выглядит как готовый продукт')
    about_text = models.TextField('Текст страницы О проекте', default='Проект помогает дизайнеру не терять заявки в переписках: клиент оформляет заказ через сайт, загружает материалы и видит статус выполнения.')
    about_feature_services = models.CharField('О проекте — услуги', max_length=180, default='цены, сроки и подробные описания')
    about_feature_portfolio = models.CharField('О проекте — портфолио', max_length=180, default='категории, кейсы и featured-блок')
    about_feature_orders = models.CharField('О проекте — заказы', max_length=180, default='файлы, статусы, финальный результат')

    contacts_title = models.CharField('Контакты — заголовок', max_length=140, default='Связь с дизайнером')
    contacts_text = models.TextField('Контакты — текст', default='Можно написать напрямую, но лучше сразу оформить заказ — так ТЗ и файлы не потеряются.')
    telegram = models.CharField('Telegram', max_length=80, default='@designer')
    email = models.EmailField('Email', default='hello@designflow.test')
    response_time = models.CharField('Время ответа', max_length=100, default='обычно в течение дня')
    footer_text = models.CharField('Текст в футере', max_length=180, default='Студия графического и digital-дизайна.')

    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
