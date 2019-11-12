"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sentry_sdk

from .base import *  # NOQA
from sentry_sdk.integrations.django import DjangoIntegration


DEBUG = False
LOG_LEVEL = os.getenv("LOG_LEVEL", "WARN").upper()
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

STATIC_URL = "https://static.eduzen.com.ar/"
MEDIA_URL = "https://media.eduzen.com.ar/"

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

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
SERVER_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get("MAILGUN_API_KEY"),
}
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'

sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[DjangoIntegration()])

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": (
                "[DJANGO] %(levelname)s %(asctime)s %(module)s "
                "%(name)s.%(funcName)s:%(lineno)s: %(message)s"
            )
        },
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {'format': '%(levelname)s %(message)s'},
    },
    "handlers": {
        "console": {"level": LOG_LEVEL, "class": "logging.StreamHandler", "formatter": "verbose"},
        'file': {
            'level': LOG_LEVEL,
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose',
        },
    },
    "loggers": {
        "*": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': False,
            'level': LOG_LEVEL,
        },
    },
}
