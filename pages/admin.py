from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Бренд и SEO', {'fields': ('site_name', 'logo_text', 'tagline', 'meta_description', 'footer_text')}),
        ('Главный экран', {'fields': ('hero_badge', 'hero_title', 'hero_text', 'primary_cta_text', 'secondary_cta_text')}),
        ('Карточка на главной', {'fields': ('hero_card_label', 'hero_card_title', 'hero_card_text', 'hero_card_price')}),
        ('Статистика на главной', {'fields': ('stat_one_value', 'stat_one_label', 'stat_two_value', 'stat_two_label', 'stat_three_value', 'stat_three_label')}),
        ('Блок услуг', {'fields': ('services_kicker', 'services_title', 'services_text')}),
        ('Блок портфолио', {'fields': ('portfolio_kicker', 'portfolio_title', 'portfolio_text')}),
        ('Финальный CTA', {'fields': ('cta_label', 'cta_title', 'cta_text', 'cta_button_text')}),
        ('О проекте', {'fields': ('about_title', 'about_text', 'about_feature_services', 'about_feature_portfolio', 'about_feature_orders')}),
        ('Контакты', {'fields': ('contacts_title', 'contacts_text', 'telegram', 'email', 'response_time')}),
        ('Системное', {'fields': ('updated_at',)}),
    )
    readonly_fields = ('updated_at',)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
