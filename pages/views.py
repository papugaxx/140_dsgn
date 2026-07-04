from django.shortcuts import render
from services.models import Service
from portfolio.models import PortfolioItem


def home(request):
    services = Service.objects.filter(is_active=True).order_by('title')[:4]
    featured_items = PortfolioItem.objects.select_related('category').filter(is_featured=True)[:6]
    latest_items = PortfolioItem.objects.select_related('category').all()[:6]
    portfolio_items = featured_items if featured_items.exists() else latest_items
    return render(request, 'pages/home.html', {'services': services, 'portfolio_items': portfolio_items})


def about(request):
    return render(request, 'pages/about.html')


def contacts(request):
    return render(request, 'pages/contacts.html')
