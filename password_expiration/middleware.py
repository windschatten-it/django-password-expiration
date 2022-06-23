from datetime import timedelta

from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.safestring import mark_safe

from password_expiration.conf import settings
from password_expiration.models import PasswordChanged
from password_expiration.utils import is_password_expired, is_password_expires_soon


class PasswordExpirationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if not request.path in settings.PASSWORD_EXPIRATION_EXCLUDE_PATHS and request.user.is_authenticated:

            if is_password_expired(request.user):
                messages.error(request, settings.PASSWORD_EXPIRATION_MESSAGES_PASSWORD_EXPIRED)
                return redirect(settings.PASSWORD_EXPIRATION_PASSWORD_CHANGE_URL)

            if is_password_expires_soon(request.user, settings.PASSWORD_EXPIRATION_SOON_AFTER_DAYS[-1]):
                msg = mark_safe(settings.PASSWORD_EXPIRATION_MESSAGES_PASSWORD_EXPIRES_SOON % (
                    self.get_remaining_days(request.user), settings.PASSWORD_EXPIRATION_PASSWORD_CHANGE_URL))
                messages.warning(request, msg)

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        if request.path == settings.PASSWORD_EXPIRATION_PASSWORD_CHANGE_DONE_URL:
            password_changed, _ = PasswordChanged.objects.get_or_create(user=request.user)
            password_changed.save()

        return response

    def get_remaining_days(self, user):
        password_changed = PasswordChanged.objects.get(user=user)
        end = password_changed.updated_on + timedelta(days=settings.PASSWORD_EXPIRATION_AFTER_DAYS)
        begin = timezone.now()
        delta = end - begin
        return delta.days
