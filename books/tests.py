from django.test import TestCase
from django.urls import reverse, resolve

from .models import Book
from .views import BookListView, BookDetailView


class BookTests(TestCase):
    """ A test class to test Books app models and views """

    def setUp(self) -> None:
        self.book = Book.objects.create(
            title='The fifth discipline',
            author='Peter M. Senge',
            price='50.00'
        )

    def test_book_created(self):
        self.assertEqual(self.book.title, 'The fifth discipline')
        self.assertEqual(self.book.author, 'Peter M. Senge')
        self.assertEqual(self.book.price, '50.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('books:book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The fifth discipline')
        self.assertNotContains(response, 'My new book')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_url_resolves_booklistview(self):
        view = resolve('/books/')
        self.assertEqual(
            view.func.__name__,
            BookListView.as_view().__name__
        )

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/1234')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'The fifth discipline')
        self.assertNotContains(response, 'The go programming language')
        self.assertTemplateUsed(response, 'books/book_detail.html')

    def test_book_detail_url_resolves_bookdetailview(self):
        view = resolve(self.book.get_absolute_url())
        self.assertEqual(
            view.func.__name__,
            BookDetailView.as_view().__name__
        )
