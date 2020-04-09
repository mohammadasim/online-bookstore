from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from order_items.models import OrderItem
from orders.models import CustomerOrder
from payments.models import CustomerPayment
from .models import Book
from .views import BookListView, BookDetailView


class BookTests(TestCase):
    """ A test class to test Books app models and views """

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='review_user',
                                                         email='user@email.com',
                                                         password='testpass123')
        self.book = Book.objects.create(
            title='The fifth discipline',
            author='Peter M. Senge',
            price=50.00,
            quantity=10
        )

    def test_book_created(self):
        self.assertEqual(self.book.title, 'The fifth discipline')
        self.assertEqual(self.book.author, 'Peter M. Senge')
        self.assertEqual(self.book.price, 50.00)
        self.assertEqual(self.book.quantity, 10)

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

    def test_book_quantity_decrement_when_ordered(self):
        self.payment_id = CustomerPayment.objects.create(
            customer_id=self.user
        )
        self.order = CustomerOrder.objects.create(
            customer_id=self.user,
            payment_id=self.payment_id
        )

        self.order_item = OrderItem.objects.create(
            book=self.book,
            quantity=3,
            order_id=self.order
        )
        book = Book.objects.get(title=self.book.title)
        self.assertEqual(book.quantity, 7)
