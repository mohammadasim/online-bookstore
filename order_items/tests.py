from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from books.models import Book
from orders.models import CustomerOrder
from payments.models import CustomerPayment
from .models import OrderItem


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
            price=50.00,
            quantity=10
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
        self.client = Client()
        self.client.force_login(self.user)

    def test_created(self):
        self.assertEqual(self.order_item.book, self.book)
        self.assertEqual(self.order_item.order_id, self.order)
        self.assertEqual(self.order_item.quantity, 3)
        self.assertEqual(self.order_item.price, self.book.price * self.order_item.quantity)

    def test_order_item_create_view_get(self):
        """
        Test logged in user can create an order_item
        """
        response = self.client.get(self.book.get_add_to_cart_url(), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_items/order_item_create.html')
        self.assertContains(response, self.order_item.book.title)
        self.assertContains(response, 'Order Book')
        self.assertNotContains(response, 'Hello World')

    def test_order_item_create_view_post(self):
        new_book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price=50.00,
            quantity=10
        )
        response = self.client.post(new_book.get_add_to_cart_url(), {
            'book': new_book,
            'quantity': 1,
            'order_id': self.order
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(OrderItem.objects.all().count(), 2)
        order_item = OrderItem.objects.get(book=new_book)
        self.assertEqual(order_item.book, new_book)
        self.assertEqual(order_item.quantity, 1)

    def test_order_item_update_get(self):
        response = self.client.get(self.order_item.get_update_url(), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_items/order_item_update.html')

    def test_order_item_update_post_increment(self):
        response = self.client.post(self.order_item.get_update_url(), {
            'book': self.book,
            'quantity': 5,
            'order_id': self.order
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        order_item = OrderItem.objects.get(book=self.book)
        self.assertEqual(order_item.quantity, 5)
