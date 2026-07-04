from django.shortcuts import get_object_or_404, render

from .models import PortfolioCategory, PortfolioItem


def portfolio_list(request):
    categories = PortfolioCategory.objects.all()
    selected_category = request.GET.get('category')
    items = PortfolioItem.objects.select_related('category')

    current_category = None
    if selected_category:
        current_category = get_object_or_404(PortfolioCategory, slug=selected_category)
        items = items.filter(category=current_category)

    return render(request, 'portfolio/portfolio_list.html', {
        'categories': categories,
        'items': items,
        'current_category': current_category,
    })


def portfolio_detail(request, slug):
    item = get_object_or_404(PortfolioItem.objects.select_related('category'), slug=slug)
    related_items = PortfolioItem.objects.select_related('category').exclude(id=item.id)[:3]
    return render(request, 'portfolio/portfolio_detail.html', {
        'item': item,
        'related_items': related_items,
    })
