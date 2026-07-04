from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from orders.models import Order
from .forms import UserRegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Аккаунт создан. Теперь можно оформить заказ.')
            return redirect('accounts:profile')
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    user_orders = Order.objects.filter(user=request.user).select_related('service').order_by('-created_at')
    return render(request, 'accounts/profile.html', {
        'orders': user_orders[:5],
        'orders_count': user_orders.count(),
    })