from easysettings import AppSettings


class Settings(AppSettings):
    """
    Default Settings for django-auth-policies
    """

    PASSWORD_INCORRECT_ATTEMPTS = 5
    PASSWORD_EXPIRES_AFTER_DAYS = 30
    PASSWORD_EXPIRES_SOON_AFTER_DAYS = 5

    PASSWORD_CHANGE_URL = '/admin/password_change/'
    PASSWORD_CHANGE_DONE_URL = '/admin/password_change/done/'
    LOGOUT_URL = '/admin/logout/'
    LOGIN_URL = '/admin/login/'
    JSI18N_URL = '/admin/jsi18n/'

    EXCLUDE_PATHS = (PASSWORD_CHANGE_URL, PASSWORD_CHANGE_DONE_URL, LOGIN_URL, LOGOUT_URL, JSI18N_URL)

    MESSAGES_PASSWORD_EXPIRED = "Your password is expired and must be changed."
    MESSAGES_PASSWORD_EXPIRES_SOON = "Your password expires in %s days."


settings = Settings()
