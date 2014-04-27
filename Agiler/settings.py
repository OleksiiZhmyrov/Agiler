"""
Django settings for Agiler project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

PROJECT_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_DIR = os.path.join(BASE_DIR, 'env')

SECRET_KEY = 'gl381ea@ouv9l5jtdhdqlt0!==u%y23rxg)0@)c3g%skkdzxb-'

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'retro',
    'core',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'Agiler.urls'

WSGI_APPLICATION = 'Agiler.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ENV_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),
    os.path.join(PROJECT_ROOT, 'ui/templates/'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'ui/static/'),
    os.path.join(PROJECT_ROOT, 'static/distrib/'),
    os.path.join(PROJECT_ROOT, 'static/temp/')
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'PAGINATE_BY': 10
}

APPEND_SLASH = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] [%(asctime)s] Module:%(module)s Process:%(process)d Thread:%(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'env/logs/debug.log'),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'env/fixtures/'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(ENV_DIR, 'cache'),
        'TIMEOUT': 60 * 30,
    }
}