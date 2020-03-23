import uuid

from django.contrib.auth import get_user_model
from django.db import models

from books.models import Book
from payments.models import CustomerPayment


class CustomerOrders(models.Model):
    """
    A model representing a customer order in the application
    """
    ORDER_STATUS = (
        ('PND', 'Pending'),
        ('CNF', 'CONFIRMED'),
        ('AWD', 'AWAITING DELIVERY'),
        ('DLD', 'DELIVERED'),
    )
    order_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    customer_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='orders',
        default=''
    )
    payment_id = models.ForeignKey(
        CustomerPayment,
        on_delete=models.CASCADE,
        related_name='order_for_the_payment'
    )
    order_status = models.CharField(
        max_length=5,
        choices=ORDER_STATUS
    )
    order_date = models.DateField(
        'Order Date',
        auto_now_add=True
    )
    order_price = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )

    def __str__(self):
        return str(self.order_id)


class CustomerOrderProduct(models.Model):
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
                                   on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=4)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
