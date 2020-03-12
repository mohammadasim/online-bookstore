from django.contrib.auth import get_user_model
from django.test import TestCase

from books.models import Book
from .models import Review


class ReviewTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='review.user@email.com',
            password='testpass123'
        )
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00'
        )
        self.review = Review.objects.create(
            book=self.book,
            title='A nice book',
            type='POS',
            review='A very nice book. Enjoyed it.',
            author=self.user
        )

    def test_book(self):
        self.assertEqual(f)
