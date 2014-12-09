DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 'this is a not very secret key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'verlustdernacht',
        'USER': 'verlustdernacht',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
    'lightcurve': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lightcurve',
        'USER': 'lightcurve'
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
