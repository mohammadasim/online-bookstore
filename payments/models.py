import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


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
        on_delete=models.SET_DEFAULT,
        related_name='payments',
        default=''
    )
    payment_date = models.DateField(
        'Payment Date',
        auto_now_add=True
    )

    def __str__(self):
        return str(self.payment_id)

    def get_absolute_url(self):
        """
        A method to return url for a payment, with payment_id
        in the url.
        """
        return reverse('payment_detail', args=[str(self.payment_id)])
