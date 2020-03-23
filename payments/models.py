import uuid

from django.contrib.auth import get_user_model
from django.db import models


class CustomerPayment(models.Model):
    """
    A django model representing a payment made by a customer
    """
    payment_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    customer_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='orders'
    )
    payment_date = models.DateField(
        'Payment Date',
        auto_now_add=True
    )
