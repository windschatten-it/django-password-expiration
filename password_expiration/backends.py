from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from password_expiration.conf import settings
from password_expiration.models import WrongPasswordEntries

UserModel = get_user_model()


class PasswordExpirationBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            qs = WrongPasswordEntries.objects.filter(user=user)

            if user.check_password(password) and self.user_can_authenticate(user):
                qs.delete()
                return user

            if not user.check_password(password) and self.user_can_authenticate(user):

                if not user.is_superuser and qs.count() < settings.PASSWORD_INCORRECT_ATTEMPTS - 1:
                    WrongPasswordEntries.objects.create(user=user)
                else:
                    user.is_active = False
                    user.save()
                    qs.delete()
                return
