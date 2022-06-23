# Create your tests here.
from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from django.test import TestCase

from password_expiration.conf import settings
from password_expiration.models import PasswordChanged
from password_expiration.utils import get_users_with_expired_password, get_users_with_expires_soon_password


class PasswordExpirationTest(TestCase):
    def test_get_users_with_expired_password(self) -> None:
        user1 = User.objects.create_user("user1", "user1@email.com")
        User.objects.create_user("user2", "user2@email.com")
        User.objects.create_user("user3", "user3@email.com")

        PasswordChanged.objects.create(user=user1, sent_expired_mail_on=timezone.now())
        PasswordChanged.objects.filter(user=user1).update(updated_on=timezone.now() - timedelta(
            days=settings.PASSWORD_EXPIRATION_AFTER_DAYS + 1))

        users_with_expired_password = get_users_with_expired_password()
        self.assertTrue(len(users_with_expired_password) == 2)

    def test_get_users_with_expires_soon_password(self) -> None:
        user1 = User.objects.create_user("user1", "user1@email.com")
        user2 = User.objects.create_user("user2", "user2@email.com")
        user3 = User.objects.create_user("user3", "user3@email.com")
        user4 = User.objects.create_user("user4", "user3@email.com")

        PasswordChanged.objects.create(user=user1)
        PasswordChanged.objects.create(user=user2)
        PasswordChanged.objects.create(user=user3)
        PasswordChanged.objects.create(user=user4)

        PasswordChanged.objects.filter(user_id=user1.id).update(updated_on=timezone.now() - timedelta(
            days=settings.PASSWORD_EXPIRATION_SOON_AFTER_DAYS[0] + 1), sent_expires_soon_mail_on=timezone.now())

        PasswordChanged.objects.filter(user=user2).update(updated_on=timezone.now() - timedelta(
            days=settings.PASSWORD_EXPIRATION_SOON_AFTER_DAYS[1] + 1),
                                                          sent_expires_soon_mail_on=timezone.now() - timedelta(days=8))

        PasswordChanged.objects.filter(user=user3).update(updated_on=timezone.now() - timedelta(
            days=settings.PASSWORD_EXPIRATION_SOON_AFTER_DAYS[2] + 1))

        PasswordChanged.objects.filter(user=user4).update(updated_on=timezone.now() - timedelta(
            days=1))
        users_with_expires_soon_password = get_users_with_expires_soon_password()
        self.assertEqual(len(users_with_expires_soon_password), 2)
