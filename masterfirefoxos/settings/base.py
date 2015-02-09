"""
Django settings for masterfirefoxos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
from collections import OrderedDict

from django.utils.translation import ugettext_lazy as _

import dj_database_url
from decouple import Csv, config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

TEMPLATE_DEBUG = config('DEBUG', default=DEBUG, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    # Third party apps
    'mptt',
    'feincms',
    'feincms.module.page',
    'feincms.module.medialibrary',
    'django_extensions',
    'django_stackato',
    'sorl.thumbnail',
    'storages',

    # Project specific apps
    'masterfirefoxos.base',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

for app in config('EXTRA_APPS', default='', cast=Csv()):
    INSTALLED_APPS.append(app)


MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'csp.middleware.CSPMiddleware',
    'masterfirefoxos.base.middleware.NonExistentLocaleRedirectionMiddleware',
)

ROOT_URLCONF = 'masterfirefoxos.urls'

WSGI_APPLICATION = 'masterfirefoxos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        cast=dj_database_url.parse
    )
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = config('USE_I18N', default=True, cast=bool)

USE_L10N = config('USE_L10N', default=True, cast=bool)

USE_TZ = config('USE_TZ', default=True, cast=bool)

STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(BASE_DIR, 'static'))
STATIC_URL = config('STATIC_URL', '/static/')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))
MEDIA_URL = config('MEDIA_URL', '/media/')

SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=not DEBUG, cast=bool)

TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Django-CSP
CSP_DEFAULT_SRC = (
    "'self'",
    "https://*.youtube.com",
    "http://*.youtube.com",
    'https://pontoon.mozilla.org',
    'https://pontoon-dev.allizom.org',
)
CSP_FONT_SRC = (
    "'self'",
    'http://*.mozilla.net',
    'https://*.mozilla.net'
)
CSP_FRAME_SRC = (
    "'self'",
    'www.googletagmanager.com',
)
CSP_IMG_SRC = (
    "'self'",
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'https://masterfirefoxos-dev.s3.amazonaws.com',
    'https://masterfirefoxos-prod.s3.amazonaws.com',
    'https://pontoon.mozilla.org',
    'https://pontoon-dev.allizom.org',
)
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-eval'",
    "'unsafe-inline'",
    'http://www.mozilla.org',
    'https://www.mozilla.org',
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'https://pontoon.mozilla.org',
    'https://pontoon-dev.allizom.org',
    'www.googletagmanager.com',
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    'http://www.mozilla.org',
    'https://www.mozilla.org',
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'https://pontoon.mozilla.org',
    'https://pontoon-dev.allizom.org',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'masterfirefoxos.base.context_processors.settings',
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('bn', _('Bengali')),
    ('hr', _('Croatian')),
    ('cs', _('Czech')),
    ('en', _('English')),
    ('de', _('German')),
    ('el', _('Greek')),
    ('hi', _('Hindi')),
    ('hu', _('Hungarian')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
    ('pl', _('Polish')),
    ('pt', _('Portuguese')),
    ('sr', _('Serbian')),
    ('es', _('Spanish')),
    ('ta', _('Tamil')),
    ('xx', _('Pirate')),
)
LANGUAGE_NAMES = dict(LANGUAGES)

VERSIONS_LOCALE_MAP = OrderedDict()
VERSIONS_LOCALE_MAP['1.1'] = {
    'slug': '1-1',
    'locales': [
        'en', 'hr', 'cs', 'de', 'el', 'hu', 'it', 'pl', 'pt', 'sr', 'es'
    ]}
VERSIONS_LOCALE_MAP['1.3T'] = {
    'slug': '1-3T',
    'locales': ['en', 'hi', 'ta']}
VERSIONS_LOCALE_MAP['1.4'] = {
    'slug': '1-4',
    'locales': ['en', 'bn']}
VERSIONS_LOCALE_MAP['2.0'] = {
    'slug': '2-0',
    'locales': ['en', 'de', 'ja']}

LOCALE_LATEST_VERSION = {}
for name, version in VERSIONS_LOCALE_MAP.items():
    for locale in version['locales']:
        LOCALE_LATEST_VERSION[locale] = {
            'slug': version['slug'],
            'name': name,
            }

SSLIFY_DISABLE = config('DISABLE_SSL', default=DEBUG, cast=bool)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')

if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_STORAGE_BUCKET_NAME:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

MIGRATION_MODULES = {
    'medialibrary': 'masterfirefoxos.base.migrate.medialibrary',
    'page': 'masterfirefoxos.base.migrate.page',
}


def media_files_unique_path(instance, filename):
    import os
    import uuid
    filename, ext = os.path.splitext(filename)
    return 'medialibrary/{}.{}{}'.format(filename, uuid.uuid4(), ext)


FEINCMS_MEDIALIBRARY_UPLOAD_TO = media_files_unique_path


THUMBNAIL_PRESERVE_FORMAT = True

LOCALIZATION_HOST = config('LOCALIZATION_HOST', default=None)
