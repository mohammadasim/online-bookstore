import uuid

from django.db import models
from django.urls import reverse

from .helpers import UniqueFilePath


class Book(models.Model):
    """ A model class representing a book in the book store """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField('Title Slug',
                            max_length=300,
                            blank=True)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to=UniqueFilePath(slug), blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        A method to return url for a book, with book's primary key
        in the url. This url is used to get BookDetailView
        """
        return reverse('book_detail', args=[str(self.id)])
