import uuid

from django.db import models
from django.urls import reverse

from books.models import Book
from orders.models import CustomerOrder


class OrderItems(models.Model):
    """
    A model representing a product ordered by a customer
    A customerOrderProduct is for an individual product
    an order can have 1 or many CustomerOrderProducts
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    product_id = models.ForeignKey(Book,
                                   on_delete=models.PROTECT)  # raises an error when deleting a product
    # that we have an order for.
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0.00
    )
    order_id = models.ForeignKey(CustomerOrder,
                                 on_delete=models.CASCADE,
                                 related_name='order_items')

    def __str__(self):
        return str(self.product_id.title)

    def save(self, *args, **kwargs):
        pass

    def get_absolute_url(self):
        """
        A method to get a customer's order for a product
        with the primary key of this order in the url
        """
        return reverse('order_product_detail', args=[str(self.id)])
