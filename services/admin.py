from django.contrib import admin
from django.utils.html import format_html
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'price_from', 'delivery_time', 'is_active', 'created_at')
    list_display_links = ('image_preview', 'title')
    list_editable = ('price_from', 'delivery_time', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'short_description', 'description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'image_preview_large')
    fieldsets = (
        ('Основное', {'fields': ('title', 'slug', 'short_description', 'description')}),
        ('Коммерция', {'fields': ('price_from', 'delivery_time', 'is_active')}),
        ('Медиа', {'fields': ('image', 'image_preview_large')}),
        ('Системное', {'fields': ('created_at',)}),
    )

    @admin.display(description='Превью')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:48px;height:48px;object-fit:cover;border-radius:12px;" />', obj.image.url)
        return '—'

    @admin.display(description='Превью изображения')
    def image_preview_large(self, obj):
        if obj and obj.image:
            return format_html('<img src="{}" style="max-width:360px;border-radius:16px;" />', obj.image.url)
        return 'Изображение не загружено'
