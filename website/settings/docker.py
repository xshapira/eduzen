"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from .base import show_toolbar
from .base import *  # NOQA


DEBUG = os.getenv("DEBUG", False) in ("True", "true", "on")
ALLOWED_HOSTS = ["*"]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mailhog'  # Your Mailhog Host
EMAIL_PORT = '1025'
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware", "pyinstrument.middleware.ProfilerMiddleware"]  # NOQA
INSTALLED_APPS += ["debug_toolbar"]  # NOQA

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
        "HOST": os.environ.get("DB_SERVICE"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": os.environ.get("MAILGUN_SENDER_DOMAIN"),
}

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARN").upper()
SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_PRINT_SQL_TRUNCATE = None
