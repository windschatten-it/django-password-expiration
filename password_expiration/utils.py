from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils import timezone

from password_expiration.conf import settings
from password_expiration.models import PasswordChanged


def is_password_expired(user: get_user_model) -> bool:
    try:
        password_changed = PasswordChanged.objects.get(user=user)
    except PasswordChanged.DoesNotExist:
        return True
    return timezone.now() > (password_changed.updated_on + timedelta(days=settings.PASSWORD_EXPIRATION_AFTER_DAYS))


def is_password_expires_soon(user: get_user_model, diff_days: int):
    try:
        password_changed = PasswordChanged.objects.get(user=user)
    except PasswordChanged.DoesNotExist:
        return True

    diff_date = password_changed.updated_on + timedelta(days=diff_days)
    return timezone.now() > diff_date


def get_users_with_expired_password() -> [get_user_model]:
    user_with_expired_password = [user for user in get_user_model().objects.all() if is_password_expired(user)]
    informed_user_with_expired_password = [password_changed.user for password_changed in
                                           PasswordChanged.objects.exclude(sent_expired_mail_on__isnull=True).filter(
                                               user__in=user_with_expired_password)]

    return [user for user in user_with_expired_password if user not in informed_user_with_expired_password]


def get_users_with_expires_soon_password() -> [get_user_model]:
    users = get_user_model().objects.all()
    user_with_expires_soon_password = []

    for diff_days in settings.PASSWORD_EXPIRATION_SOON_AFTER_DAYS:
        _user_with_expires_soon_password = [user for user in users if is_password_expires_soon(user, diff_days)]
        informed_user_with_expires_soon_password = [password_changed.user for password_changed in
                                                    PasswordChanged.objects.exclude(
                                                        Q(sent_expires_soon_mail_on__isnull=True) | Q(
                                                            sent_expires_soon_mail_on__lt=timezone.now() - timedelta(
                                                                days=diff_days))).filter(
                                                        user__in=_user_with_expires_soon_password)]
        uninformed_users = [user for user in _user_with_expires_soon_password if
                            user not in informed_user_with_expires_soon_password and
                            user not in user_with_expires_soon_password]
        user_with_expires_soon_password += uninformed_users
    return user_with_expires_soon_password
