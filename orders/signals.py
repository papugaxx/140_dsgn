from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from .models import Order, OrderFile


def _delete_file(file_field):
    if file_field and file_field.name:
        file_field.delete(save=False)


@receiver(post_delete, sender=OrderFile)
def delete_order_file(sender, instance, **kwargs):
    _delete_file(instance.file)


@receiver(post_delete, sender=Order)
def delete_final_file_on_order_delete(sender, instance, **kwargs):
    _delete_file(instance.final_file)


@receiver(pre_save, sender=Order)
def replace_final_file(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Order.objects.get(pk=instance.pk)
    except Order.DoesNotExist:
        return

    if old_instance.final_file != instance.final_file:
        _delete_file(old_instance.final_file)