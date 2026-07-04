from django.contrib import admin
from django.utils.html import format_html
from .models import Order, OrderFile


class OrderFileInline(admin.TabularInline):
    model = OrderFile
    extra = 0
    readonly_fields = ('uploaded_at', 'filename_display')
    fields = ('file', 'filename_display', 'uploaded_at')

    @admin.display(description='Имя файла')
    def filename_display(self, obj):
        return obj.filename if obj and obj.file else '—'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'service', 'status_badge', 'price', 'deadline', 'created_at')
    list_display_links = ('id', 'title')
    list_editable = ('price', 'deadline')
    list_filter = ('status', 'service', 'created_at', 'deadline')
    search_fields = ('title', 'description', 'contact', 'user__username', 'user__email')
    autocomplete_fields = ('user', 'service')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Клиент и задача', {'fields': ('user', 'service', 'title', 'description', 'contact')}),
        ('Управление заказом', {'fields': ('status', 'price', 'deadline', 'admin_comment', 'final_file')}),
        ('Системная информация', {'fields': ('created_at', 'updated_at')}),
    )
    inlines = [OrderFileInline]

    @admin.display(description='Статус', ordering='status')
    def status_badge(self, obj):
        colors = {
            Order.Status.NEW: '#64748b',
            Order.Status.REVIEW: '#d97706',
            Order.Status.ACCEPTED: '#2563eb',
            Order.Status.WAITING_PAYMENT: '#9333ea',
            Order.Status.IN_PROGRESS: '#0f766e',
            Order.Status.DONE: '#15803d',
            Order.Status.REJECTED: '#dc2626',
        }
        color = colors.get(obj.status, '#64748b')
        return format_html('<span style="background:{};color:#fff;border-radius:999px;padding:4px 10px;font-weight:700;">{}</span>', color, obj.get_status_display())


@admin.register(OrderFile)
class OrderFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'file', 'uploaded_at')
    list_display_links = ('id', 'file')
    search_fields = ('order__title', 'file')
    readonly_fields = ('uploaded_at',)
