from django.conf import settings
from django.db import models


class WrongPasswordEntries(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entered_on = models.DateTimeField(auto_now_add=True)


class PasswordChanged(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    sent_expired_mail_on = models.DateTimeField(blank=True, null=True, default=None)
    sent_expires_soon_mail_on = models.DateTimeField(blank=True, null=True, default=None)