from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve

from books.models import Book
from orders.models import CustomerOrder
from payments.models import CustomerPayment
from .models import OrderItem
from .views import order_item_create_view


class OrderItemTests(TestCase):
    """
    A test class to test order_items app, its models and views
    """

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='review_user',
                                                         email='user@email.com',
                                                         password='testpass123')
        self.book = Book.objects.create(
            title='Deep work',
            author='Cal Newport',
            price=50.00
        )
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

    def test_created(self):
        self.assertEqual(self.order_item.book, self.book)
        self.assertEqual(self.order_item.order_id, self.order)
        self.assertEqual(self.order_item.quantity, 3)
        self.assertEqual(self.order_item.price, self.book.price * self.order_item.quantity)

    def test_order_item_create_view(self):
        """
        Test logged in user can create an order_item
        """
        self.client.force_login(self.user)
        response = self.client.get(self.book.get_add_to_cart_url(), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_items/order_item_create.html')
        self.assertContains(response, self.order_item.book.title)
        self.assertContains(response, 'Order Book')
        self.assertNotContains(response, 'Hello World')
        response = self.client.post(self.book.get_add_to_cart_url(), {
            'book': self.book,
            'quantity': 1
        }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_order_item_create_item_order_resolves_order_item_create_view(self):
        view = resolve(self.book.get_add_to_cart_url())
        self.assertEqual(
            view.func.__name__,
            order_item_create_view.as_view().__name__
        )
