from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating user with an email is succesfull"""
        email = "test@unittest.com"
        password = "StringPassword"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_by_email_nomalizers(self):
        """Test creating user with an email nomalizer"""
        email = 'test@UNITTEST.COM'
        user = get_user_model().objects.create_user(email, 'test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_super_user(
            'test@unittest.com',
            'test1234'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
