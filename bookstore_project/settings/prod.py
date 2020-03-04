from .base import *

DEBUG = False

ALLOWED_HOSTS = ["app"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PGSQL_DB_NAME'),
        'USER': os.environ.get('PGSQL_DB_USER'),
        'PASSWORD': os.environ.get('PGSQL_DB_PASW'),
        'HOST': os.environ.get('PGSQL_DB_HOST'),
        'PORT': os.environ.get('PGSQL_DB_PORT')
    }
}
LOGIN_REDIRECT_URL = 'home'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
