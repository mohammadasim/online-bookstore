from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


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


class SignupTests(TestCase):
    """
    Test class to test signup process provided by django allauth
    """
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self) -> None:
        """ Overriding the setup method to create a response object """
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        """ Test suite for signup Template """
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hello world')

    def test_signup_form(self):
        """
        Test to ensure that user is created with correct
        username and email.
        Django creates test database and destroys it hence the index 0
        in test.
        """
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
