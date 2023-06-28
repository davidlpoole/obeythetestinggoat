from django.contrib import auth
from django.test import TestCase

from accounts.models import Token

User = auth.get_user_model()


class UserModelTest(TestCase):
    def test_user_is_valid_with_email_only(self):
        user = User(email="edith@example.com")
        user.full_clean()  # should not raise

    def test_email_is_primary_key(self):
        user = User(email="edith@example.com")
        self.assertEqual(user.pk, "edith@example.com")


class TokenModelTest(TestCase):
    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email="edith@example.com")
        token2 = Token.objects.create(email="edith@example.com")
        self.assertNotEqual(token1.uid, token2.uid)
