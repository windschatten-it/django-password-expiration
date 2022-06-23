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

## Changelog

See [CHANGELOG.md](https://github.com/windschatten-it/django-password-expiration/tree/master/CHANGELOG.md).

## License

MIT