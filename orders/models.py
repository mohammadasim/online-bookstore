import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum
from django.urls import reverse

from payments.models import CustomerPayment


class CustomerOrder(models.Model):
    """
    A model representing a customer order in the application
    """
    ORDER_STATUS = (
        ('PND', 'Pending'),
        ('PAD', 'PAID'),
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
        on_delete=models.SET_DEFAULT,
        related_name='orders',
        default='anonymous'
    )
    payment_id = models.ForeignKey(
        CustomerPayment,
        on_delete=models.CASCADE,
        related_name='payment_for_order',
        blank=True
    )
    order_status = models.CharField(
        max_length=3,
        choices=ORDER_STATUS,
        default='PND'
    )
    order_date = models.DateField(
        'Order Date',
        auto_now_add=True
    )
    order_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0.00
    )

    def __str__(self):
        return str(self.order_id)

    def save(self, *args, **kwargs):
        order_items = self.order_items  # order_items is reverse relationship defined in order_item model
        # Using django aggregate and sum tools we calculate
        # the price of the order, we are using reverse relationship again.
        self.order_price = order_items.aggregate(Sum('price')) if order_items.exists() else 0.00
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        A method to return url for an order, with 
        order_id in the url
        """
        return reverse('order_detail', args=[str(self.order_id)])
