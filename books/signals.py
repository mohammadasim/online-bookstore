"""
Signal.py holds signals for Book app. Django docs advice against putting
signal code in models.
"""

from django.db.models.signals import post_delete, post_save
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


@receiver(post_save, sender=OrderItem)
def update_book_quantity_when_order_is_placed(sender, instance, **kwargs):
    """
    A receiver function that listens for post_save signal from orderitem.
    When an order is placed for a book, we must update the quantity of the book
    to reflect the change.
    The signal is sent by order_items and hence is the instance
    The signal is received by book and hence is the receiver
    """
    book = instance.book
    book.quantity -= instance.quantity
    book.save()
