from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from orders.models import Order
from services.models import Service
from portfolio.models import PortfolioCategory, PortfolioItem
from pages.models import SiteSettings


class Command(BaseCommand):
    help = 'Создаёт демо-услуги, портфолио, пользователей и заказы'

    def handle(self, *args, **options):
        User = get_user_model()

        services = [
            {'title': 'Логотип', 'slug': 'logo-design', 'short_description': 'Разработка узнаваемого логотипа для бренда, канала или проекта.', 'description': 'Создание логотипа под задачу клиента: анализ референсов, подбор стилистики, подготовка финального варианта и файлов для использования.', 'price_from': 1200, 'delivery_time': '2–4 дня'},
            {'title': 'Баннер', 'slug': 'banner-design', 'short_description': 'Баннеры для Telegram, YouTube, сайтов и рекламных креативов.', 'description': 'Разработка баннера с акцентом на читаемость, композицию и цель публикации. Подходит для обложек, анонсов и промо.', 'price_from': 700, 'delivery_time': '1–3 дня'},
            {'title': 'Аватарка', 'slug': 'avatar-design', 'short_description': 'Стильная аватарка для личного бренда, канала или сообщества.', 'description': 'Создание аватарки с учётом тематики проекта, цветовой палитры и читаемости в маленьком размере.', 'price_from': 500, 'delivery_time': '1–2 дня'},
            {'title': '3D-дизайн', 'slug': '3d-design', 'short_description': 'Объёмные визуалы, обложки и простые 3D-композиции.', 'description': 'Подготовка 3D-визуала для соцсетей, обложки, презентации или рекламного материала.', 'price_from': 1800, 'delivery_time': '3–7 дней'},
            {'title': 'Social pack', 'slug': 'social-pack', 'short_description': 'Набор визуалов для запуска канала, постов или рекламной кампании.', 'description': 'Комплект из нескольких согласованных макетов: обложки, посты, аватарка и промо-баннеры.', 'price_from': 2500, 'delivery_time': '4–8 дней'},
            {'title': 'Редизайн макета', 'slug': 'redesign', 'short_description': 'Освежить старый макет и привести его к современному виду.', 'description': 'Аудит текущего дизайна, переработка композиции, типографики, цвета и подготовка финальных файлов.', 'price_from': 900, 'delivery_time': '1–4 дня'},
        ]
        for data in services:
            Service.objects.update_or_create(slug=data['slug'], defaults=data)

        category_map = {}
        for name, slug in [('Логотипы', 'logos'), ('Баннеры', 'banners'), ('Аватарки', 'avatars'), ('3D', '3d'), ('Digital', 'digital')]:
            category, _ = PortfolioCategory.objects.update_or_create(slug=slug, defaults={'name': name})
            category_map[slug] = category

        portfolio = [
            ('studio-logo', 'Логотип для студии', 'logos', 'Минималистичный знак для небольшой дизайн-студии.', 'Studio 140'),
            ('telegram-banner', 'Баннер для Telegram', 'banners', 'Контрастная обложка для продвижения Telegram-канала.', 'TG Launch'),
            ('brand-avatar', 'Аватарка для бренда', 'avatars', 'Стилизованная аватарка с акцентом на узнаваемость.', 'Personal Brand'),
            ('three-d-cover', '3D-обложка', '3d', 'Обложка с объёмными элементами и чистой композицией.', 'Product Cover'),
            ('youtube-preview', 'YouTube preview', 'banners', 'Обложка с фокусом на кликабельность и читаемый заголовок.', 'YouTube'),
            ('product-card', 'Карточка продукта', 'digital', 'Digital-визуал для сайта и соцсетей.', 'E-commerce'),
        ]
        for slug, title, category_slug, description, client in portfolio:
            PortfolioItem.objects.update_or_create(slug=slug, defaults={'title': title, 'category': category_map[category_slug], 'description': description, 'client': client, 'is_featured': True})

        admin, _ = User.objects.update_or_create(username='admin', defaults={'email': 'admin@designflow.test', 'first_name': 'Admin', 'is_staff': True, 'is_superuser': True})
        admin.set_password('AdminPass2026!')
        admin.save()

        client, _ = User.objects.update_or_create(username='client', defaults={'email': 'client@designflow.test', 'first_name': 'Клиент'})
        client.set_password('ClientPass2026!')
        client.save()

        Order.objects.update_or_create(user=client, title='Баннер для Telegram-канала', defaults={'service': Service.objects.get(slug='banner-design'), 'description': 'Нужен баннер 1280x720 для запуска нового Telegram-канала. Стиль: современный, контрастный, с акцентом на название.', 'contact': '@client_demo', 'status': Order.Status.IN_PROGRESS, 'price': 900, 'deadline': timezone.now().date() + timedelta(days=3), 'admin_comment': 'ТЗ принято, первый вариант будет готов завтра.'})
        Order.objects.update_or_create(user=client, title='Логотип для мини-студии', defaults={'service': Service.objects.get(slug='logo-design'), 'description': 'Нужно придумать простой логотип для небольшой дизайн-студии. Цвета: бежевый, белый, тёмный фон.', 'contact': 'client@designflow.test', 'status': Order.Status.REVIEW, 'admin_comment': 'Заявка получена, скоро уточним детали.'})

        SiteSettings.objects.update_or_create(pk=1, defaults={'site_name': 'Design Flow', 'logo_text': 'DF', 'tagline': 'Студия графического и digital-дизайна', 'hero_badge': 'Портфолио · услуги · заказы', 'hero_title': 'Дизайн для брендов, соцсетей и digital-проектов', 'hero_text': 'Выбираешь услугу, отправляешь ТЗ и материалы, а дальше отслеживаешь статус заказа в личном кабинете.', 'telegram': '@designer', 'email': 'hello@designflow.test'})

        self.stdout.write(self.style.SUCCESS('Демо-данные успешно созданы.'))
        self.stdout.write('Демо-админ: admin / AdminPass2026!')
        self.stdout.write('Демо-клиент: client / ClientPass2026!')
