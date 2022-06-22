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


Run the included migrations:

```bash
python manage.py migrate
```

To learn how to configure permissions and manage API keys, head to
the [Documentation](https://florimondmanca.github.io/djangorestframework-api-key).

## Changelog

See [CHANGELOG.md](https://github.com/florimondmanca/djangorestframework-api-key/tree/master/CHANGELOG.md).

## Contributing

See [CONTRIBUTING.md](https://github.com/florimondmanca/djangorestframework-api-key/tree/master/CONTRIBUTING.md).

## License

MIT

Enabling messages¶
Messages are implemented through a middleware class and corresponding context processor.

The default settings.py created by django-admin startproject already contains all the settings required to enable
message functionality:

'django.contrib.messages' is in INSTALLED_APPS.

MIDDLEWARE contains 'django.contrib.sessions.middleware.SessionMiddleware' and '
django.contrib.messages.middleware.MessageMiddleware'.

The default storage backend relies on sessions. That’s why SessionMiddleware must be enabled and appear before
MessageMiddleware in MIDDLEWARE.

The 'context_processors' option of the DjangoTemplates backend defined in your TEMPLATES setting contains '
django.contrib.messages.context_processors.messages'.

If you don’t want to use messages, you can remove 'django.contrib.messages' from your INSTALLED_APPS, the
MessageMiddleware line from MIDDLEWARE, and the messages context processor from TEMPLATES.