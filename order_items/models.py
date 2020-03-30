import uuid

from django.db import models
from django.urls import reverse

from books.models import Book
from orders.models import CustomerOrder


class OrderItem(models.Model):
    """
    A model representing a book ordered by a customer
    A order_item is for an individual book
    an order can have 1 or many order_items
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    book = models.ForeignKey(Book,
                             on_delete=models.PROTECT)  # raises an error when deleting a product
    # that we have an order for.
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0.00
    )
    order_id = models.ForeignKey(CustomerOrder,
                                 on_delete=models.CASCADE,
                                 related_name='order_items')

    def save(self, *args, **kwargs):
        self.price = self.book.price * self.quantity
        super().save(*args, **kwargs)
        self.order_id.save()

    def get_absolute_url(self):
        """
        A method to get a customer's order for a product
        with the primary key of this order in the url
        """
        return reverse('order_items:order_item_delete', args=[str(self.id)])

    def get_update_url(self):
        return reverse('order_items:order_item_update', args=[str(self.id)])
