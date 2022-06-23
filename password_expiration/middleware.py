from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils import timezone

from password_expiration.conf import settings
from password_expiration.models import PasswordChanged


class PasswordExpirationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if not request.path in settings.EXCLUDE_PATHS and request.user.is_authenticated:

            if self.is_password_expired(request.user):
                messages.error(request, settings.MESSAGES_PASSWORD_EXPIRED)
                return redirect(settings.PASSWORD_CHANGE_URL)

            if self.is_password_expires_soon(request.user):
                messages.warning(request,
                                 settings.MESSAGES_PASSWORD_EXPIRES_SOON % self.get_remaining_days(request.user))

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        if request.path == settings.PASSWORD_CHANGE_DONE_URL:
            password_changed, _ = PasswordChanged.objects.get_or_create(user=request.user)
            password_changed.save()

        return response

    def is_password_expired(self, user: User) -> bool:
        try:
            password_changed = PasswordChanged.objects.get(user=user)
        except PasswordChanged.DoesNotExist:
            return True
        return timezone.now() > (password_changed.updated_on + timedelta(days=settings.PASSWORD_EXPIRES_AFTER_DAYS))

    def is_password_expires_soon(self, user):
        try:
            password_changed = PasswordChanged.objects.get(user=user)
        except PasswordChanged.DoesNotExist:
            return True

        return timezone.now() > (
                password_changed.updated_on + timedelta(days=settings.PASSWORD_EXPIRES_SOON_AFTER_DAYS))

    def get_remaining_days(self, user):
        password_changed = PasswordChanged.objects.get(user=user)
        end = password_changed.updated_on + timedelta(days=settings.PASSWORD_EXPIRES_AFTER_DAYS)
        begin = timezone.now()
        delta = end - begin
        return delta.days
