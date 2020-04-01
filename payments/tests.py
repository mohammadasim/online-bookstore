from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import CustomerPayment


class CustomerPaymentTest(TestCase):
    """
    A test class to test CustomerPayment app, its views and model
    """

    def setUp(self) -> None:
        self.customer_id = get_user_model().objects.create_user(username='test_user',
                                                                email='test@email.com',
                                                                password='testPass')
        self.payment = CustomerPayment.objects.create(
            customer_id=self.customer_id
        )

    def testCreated(self):
        self.assertEqual(self.payment.customer_id, self.customer_id)
