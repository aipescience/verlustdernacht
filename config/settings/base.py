import os

from . import BASE_DIR

DEBUG = False

ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'django_extensions',
    'vendor_files',
    'api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'vendor/')
]


'''
    "angular-i18n": "^1.5.8",
    "droidsans-googlefont": "*"
'''

VENDOR = {
    'jquery': {
        'url': 'https://code.jquery.com/',
        'js': [
            {
                'path': 'jquery-3.2.1.min.js',
                'sri': 'sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=',
            }
        ]
    },
    'bootstrap': {
        'url': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/',
        'js': [
            {
                'path': 'js/bootstrap.min.js',
                'sri': 'sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa',
            }
        ],
        'css': [
            {
                'path': 'css/bootstrap.min.css',
                'sri': 'sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u',
            }
        ]
    },
    'font-awesome': {
        'url': 'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/',
        'css': [
            {
                'path': 'css/font-awesome.min.css'
            }
        ],
        'font': [
            {
                'path': 'fonts/fontawesome-webfont.eot'
            },
            {
                'path': 'fonts/fontawesome-webfont.woff2'
            },
            {
                'path': 'fonts/fontawesome-webfont.woff'
            },
            {
                'path': 'fonts/fontawesome-webfont.ttf'
            },
            {
                'path': 'fonts/fontawesome-webfont.svg'
            }
        ]
    },
    'angular': {
        'url': 'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.7.5/',
        'js': [
            {
                'path': 'angular.min.js',
                'sri': 'sha256-QRJz3b0/ZZC4ilKmBRRjY0MgnVhQ+RR1tpWLYaRRjSo='
            },
            {
                'path': 'angular-resource.min.js',
                'sri': 'sha256-ZiY1Zj/A6xFJol9+f4MleFeYUnfdNfUSHtlawW8faL8='
            },
            {
                'path': 'angular-sanitize.min.js',
                'sri': 'sha256-LLlLr1XzKUXSFI9SiuEJOAn88Dwge+/zld523N2c8+8='
            },
            {
                'path': 'i18n/angular-locale_de-de.js',
                'sri': 'sha256-fESKAxb0GoapynhnK/CEjOskdp4Yyzr+SVBc0VeHQpI='
            }
        ],
        'map': [
            {
                'path': 'angular.min.js.map'
            },
            {
                'path': 'angular-resource.min.js.map'
            },
            {
                'path': 'angular-sanitize.min.js.map'
            }
        ]
    },
    'moment': {
        'url': 'https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/',
        'js': [
            {
                'path': 'moment.min.js',
                'sri': 'sha256-1hjUhpc44NwiNg8OwMu2QzJXhD8kcj+sJA3aCQZoUjg='
            }
        ]
    },
    'd3': {
        'url': 'https://cdnjs.cloudflare.com/ajax/libs/d3/5.7.0/',
        'js': [
            {
                'path': 'd3.min.js',
                'sri': 'sha256-va1Vhe+all/yVFhzgwmwBgWMVfLHjXlNJfvsrjUBRgk='
            }
        ]
    }
}
