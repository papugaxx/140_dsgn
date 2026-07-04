from django.contrib import admin
from django.utils.html import format_html
from .models import PortfolioCategory, PortfolioItem


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'category', 'client', 'is_featured', 'created_at')
    list_display_links = ('image_preview', 'title')
    list_editable = ('category', 'is_featured')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'description', 'client')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'image_preview_large')
    fieldsets = (
        ('Кейс', {'fields': ('title', 'slug', 'category', 'client', 'description')}),
        ('Витрина', {'fields': ('image', 'image_preview_large', 'is_featured')}),
        ('Системное', {'fields': ('created_at',)}),
    )

    @admin.display(description='Превью')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:56px;height:42px;object-fit:cover;border-radius:10px;" />', obj.image.url)
        return '—'

    @admin.display(description='Превью изображения')
    def image_preview_large(self, obj):
        if obj and obj.image:
            return format_html('<img src="{}" style="max-width:420px;border-radius:16px;" />', obj.image.url)
        return 'Изображение не загружено'
