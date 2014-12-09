# -*- coding: utf-8 -*-
import os
from local import *

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'lmdb'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'verlustdernacht.urls'
WSGI_APPLICATION = 'verlustdernacht.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ROOT = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT,'static/')

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT,'verlustdernacht/static/'),
)

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT,'verlustdernacht/templates/'),
)

DATABASE_ROUTERS = ['verlustdernacht.routers.Router']
