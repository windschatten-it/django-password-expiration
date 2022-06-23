from easysettings import AppSettings
from django.conf import settings as default_settings


class Settings(AppSettings):
    """
    Default Settings for django-auth-policies
    """

    PASSWORD_EXPIRATION_INCORRECT_ATTEMPTS = 5
    PASSWORD_EXPIRATION_AFTER_DAYS = 30
    PASSWORD_EXPIRATION_SOON_AFTER_DAYS = (60, 30, 7)

    PASSWORD_EXPIRATION_PASSWORD_CHANGE_URL = '/admin/password_change/'
    PASSWORD_EXPIRATION_PASSWORD_CHANGE_DONE_URL = '/admin/password_change/done/'
    PASSWORD_EXPIRATION_LOGOUT_URL = '/admin/logout/'
    PASSWORD_EXPIRATION_LOGIN_URL = '/admin/login/'
    PASSWORD_EXPIRATION_JSI18N_URL = '/admin/jsi18n/'

    PASSWORD_EXPIRATION_EXCLUDE_PATHS = (
    PASSWORD_EXPIRATION_PASSWORD_CHANGE_URL, PASSWORD_EXPIRATION_PASSWORD_CHANGE_DONE_URL,
    PASSWORD_EXPIRATION_LOGIN_URL, PASSWORD_EXPIRATION_LOGOUT_URL, PASSWORD_EXPIRATION_JSI18N_URL)

    PASSWORD_EXPIRATION_MESSAGES_PASSWORD_EXPIRED = "Your password has expired and needs to be changed."
    PASSWORD_EXPIRATION_MESSAGES_PASSWORD_EXPIRES_SOON = "Your password will expire in %s days. " \
                                                         "<a href='%s'>Change Password</a>"

    """
    Mail settings
    """

    PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRES_SOON_SUBJECT = "Your password will expire soon."
    PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRED_SUBJECT = "Your password will expire soon and should be changed."

    PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRES_SOON_BODY = "Your password has expired."
    PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRED_BODY = "Your password has expired and needs to be changed."

    PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRATION_FROM_EMAIL = None
    PASSWORD_EXPIRATION_MAIL_PASSWORD_EXPIRATION_REPLY_TO_EMAIL = None


settings = Settings()
