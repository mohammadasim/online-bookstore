"""
signals.py holds signals for Orders app. Django docs advice against
putting signal code in models
"""
from django.db.models.signals import post_delete
from django.dispatch import receiver

from order_items.models import OrderItem


@receiver(post_delete, sender=OrderItem)
def update_order_when_order_item_deleted(sender, instance, **kwargs):
    """
    This function will be invoked with an order_item in the order is
    deleted. This function will update the total price of the order
    """
    order = instance.order_id
    order.save()
