from .models import Service


def active_services(request):
    return {
        'nav_services': Service.objects.filter(is_active=True).order_by('title')[:6]
    }
