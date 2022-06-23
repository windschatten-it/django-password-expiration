# django-password-expiration

Password expiration policy for [Django](https://docs.djangoproject.com/en/3.2/).

## Quickstart

Install with `pip`:

```bash
pip install git+https://github.com/windschatten-it/django-password-expiration.git
```

Add the app to your `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    # ...
    "django.contrib.messages",
    "password_expiration"
]
```

_**Note**: Take care 'django.contrib.messages' is in INSTALLED_APPS._

Add the middleware to your `MIDDLEWARE`:

```python
# settings.py

MIDDLEWARE = [
    # ...
    'password_expiration.middleware.PasswordExpirationMiddleware'
]
```

_**Note**: Take care MIDDLEWARE contains 'django.contrib.sessions.middleware.SessionMiddleware' and '
django.contrib.messages.middleware.MessageMiddleware'._

Add the backend to your `AUTHENTICATION_BACKENDS`:

```python
# settings.py

AUTHENTICATION_BACKENDS = ['password_expiration.backends.PasswordExpirationBackend']
```

Customize the app settings if necessary:

```python
# settings.py

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
PASSWORD_EXPIRATION_MESSAGES_PASSWORD_EXPIRES_SOON = "Your password will expire in %s days. "
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
```

Run the included migrations:

```bash
python manage.py migrate
```

Send email notifications:

```bash
python manage.py send-password-expiration-emails
```

## Changelog

See [CHANGELOG.md](https://github.com/windschatten-it/django-password-expiration/tree/master/CHANGELOG.md).

## License

MIT