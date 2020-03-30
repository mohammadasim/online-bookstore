"""
Signal.py holds signals for Book app. Django docs advice against putting
signal code in models.
"""

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from order_items.models import OrderItem


@receiver(post_delete, sender=OrderItem)
def update_book_quantity_on_order_item_delete(sender, instance, **kwargs):
    """
    A receiver function that listens for post_delete signal from orderitems.
    When an order item is deleted, we need to add the quantity of the orderitem
    back to the book quantity.
    The signal is sent by order_item and hence is the instance
    The signal is received by book and hence is the receiver
    """
    book = instance.book
    book.quantity += instance.quantity
    book.save()


@receiver(pre_save, sender=OrderItem)
def update_book_quantity_when_order_is_updated(sender, instance, **kwargs):
    """
    signal function invoked with quantity of orderItem is updated
    """
    book = instance.book
    # Check if this a new or an existing orderItem
    initial_order = OrderItem.objects.filter(id=instance.id)
    if initial_order.exists():
        # Get the initial quantity of the order from database
        initial_order_quantity = initial_order.first().quantity
        # If the orderItem quantity has increased
        if initial_order_quantity < instance.quantity:
            updated_quantity = instance.quantity - initial_order_quantity
            # subtract the updated quantity from book quantity in stock
            book.quantity -= updated_quantity
            book.save()
        # If the orderItem quantity has decreased
        elif initial_order_quantity > instance.quantity:
            quantity_difference = initial_order_quantity - instance.quantity
            book.quantity += quantity_difference
            book.save()
    else:
        book.quantity -= instance.quantity
        book.save()
