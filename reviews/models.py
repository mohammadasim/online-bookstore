import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from books.models import Book

REVIEW_TYPES = (
    ('POS', 'Positive'),
    ('NEG', 'Negative'),
    ('NEU', 'Neutral'),
)


class Review(models.Model):
    """
    A model class representing a review in the book store
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',  # name of reverse relationship, book will have reviews as a field
    )
    title = models.CharField(max_length=60)
    type = models.CharField(max_length=20,
                            choices=REVIEW_TYPES)
    review = models.TextField('Review')
    update_date = models.DateField('Last Updated',
                                   auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        """
        A method to return url for a review, with reviews's primary key
        in the url.
        """
        return reverse('review_update', args=[str(self.id)])

    def clean_book(self):
        pass
