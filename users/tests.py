from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView


class CustomUserTests(TestCase):
    """
    Test class to test User creation functionality
    """

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='tom',
            email='tom@email.com',
            password='password01'
        )
        self.assertEqual(user.username, 'tom')
        self.assertEqual(user.email, 'tom@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin_tom',
            email='admin_tom@email.com',
            password='password02'
        )
        self.assertEqual(admin_user.username, 'admin_tom')
        self.assertEqual(admin_user.email, 'admin_tom@email.com')
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)


class SignupPageTests(TestCase):
    """
    Test class to test signup page view and its functionality
    """

    def setUp(self) -> None:
        """ Overriding the setup method to create a response object """
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        """ Test suite for signup Template """
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hello world')

    def test_signup_form(self):
        """ Test suite for signup form """
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)

    def test_signup_view(self):
        """ Test suite for signup view """
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )
