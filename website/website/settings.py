"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

try:
    from .keysettings import (
        SECRET_KEY, DATABASES, NORECAPTCHA_SITE_KEY, NORECAPTCHA_SECRET_KEY,
        ANYMAIL, EMAIL_BACKEND, DEFAULT_FROM_EMAIL,
    )
except Exception:
    SECRET_KEY = "9-t+&@+bo$l263c!s_3vobwh0_1bx^m93wih^-s+bt1xljfrnv"
    NORECAPTCHA_SECRET_KEY = "some key"
    NORECAPTCHA_SITE_KEY = "some key"
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
        }
    }

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
SITE_ID = 1
APPEND_SLASH = True

DEBUG = False

ALLOWED_HOSTS = [
    'www.eduardoenriquez.com.ar', 'eduardoenriquez.com.ar',
    'eduzen.com.ar', 'www.eduzen.com.ar',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    'nocaptcha_recaptcha',
    'debug_toolbar',
    'anymail',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'solo',
    'robots',
    'djmoney',
    'rest_framework',
    'django_extensions',
    'channels',

    'config',
    'blog',
    'api',
    'expenses',
    'chat',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'full',
    },
    'default': {
        'toolbar': 'full',
        'autoParagraph': 'false',
        'breakBeforeOpen': 'false',
        'breakAfterOpen': 'false',
        'breakBeforeClose': 'false',
        'breakAfterClose': 'false',
        'enterMode': 'false',
        'extraPlugins': ','.join(
            [
                'codesnippet',
            ]),
    },
    'autoParagraph': 'false',
}

def show_toolbar(request):
    return False

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

INTERNAL_IPS = ('45.55.130.126', )

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

# Channels

ASGI_APPLICATION = "website.routing.application"
