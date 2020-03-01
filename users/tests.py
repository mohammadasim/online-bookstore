from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

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
