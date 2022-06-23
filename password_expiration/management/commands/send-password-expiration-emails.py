from django.core.mail import EmailMessage
from django.core.management import BaseCommand

from password_expiration.conf import settings
from password_expiration.utils import get_users_with_expired_password, get_users_with_expires_soon_password


class Command(BaseCommand):
    help = 'Send notification emails about Password expiration to users.'

    def handle(self, *args, **options):
        users_with_expired_password = get_users_with_expired_password()
        users_with_expires_soon_password = get_users_with_expires_soon_password()

        for user in users_with_expired_password:
            email = EmailMessage(
                settings.PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRED_SUBJECT,
                settings.PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRED_BODY,
                settings.PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRATION_FROM_EMAIL,
                [user.email],
                reply_to=[settings.PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRATION_FROM_EMAIL]
            )

            email.send(fail_silently=True)

        for user in users_with_expires_soon_password:
            email = EmailMessage(
                settings.PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRED_SUBJECT,
                settings.PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRED_BODY,
                settings.PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRATION_FROM_EMAIL,
                [user.email],
                reply_to=[settings.PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRATION_FROM_EMAIL]
            )

            email.send(fail_silently=True)
