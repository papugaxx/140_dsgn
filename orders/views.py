from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import OrderCreateForm
from .models import Order, OrderFile


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).select_related('service')
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_create(request):
    initial = {}
    service_id = request.GET.get('service')
    if service_id:
        initial['service'] = service_id

    if request.method == 'POST':
        form = OrderCreateForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    order = form.save(commit=False)
                    order.user = request.user
                    order.save()

                    for uploaded_file in form.cleaned_data.get('files', []):
                        OrderFile.objects.create(order=order, file=uploaded_file)
            except OSError:
                messages.error(request, 'Не удалось загрузить файлы. Попробуйте снова.')
            else:
                messages.success(request, 'Заказ успешно создан.')
                return redirect(order.get_absolute_url())
    else:
        form = OrderCreateForm(initial=initial)

    return render(request, 'orders/order_create.html', {'form': form})


@login_required
def order_detail(request, pk):
    order = get_object_or_404(
        Order.objects.select_related('service', 'user').prefetch_related('files'),
        pk=pk,
        user=request.user,
    )
    return render(request, 'orders/order_detail.html', {'order': order})


@login_required
def order_file_download(request, pk, file_id):
    order_file = get_object_or_404(
        OrderFile.objects.select_related('order'),
        pk=file_id,
        order_id=pk,
        order__user=request.user,
    )
    try:
        return FileResponse(order_file.file.open('rb'), as_attachment=True, filename=order_file.filename)
    except FileNotFoundError as exc:
        raise Http404('Файл не найден.') from exc


@login_required
def order_final_file_download(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    if not order.final_file:
        raise Http404('Final file does not exist.')

    filename = order.final_file.name.split('/')[-1]
    try:
        return FileResponse(order.final_file.open('rb'), as_attachment=True, filename=filename)
    except FileNotFoundError as exc:
        raise Http404('Финальный файл недоступен.') from exc