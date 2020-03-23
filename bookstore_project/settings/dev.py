from .base import *

DEBUG = True

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

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# ************************** ALL AUTH CONFIGURATION ****************************** #
# Dev email settings, enables email output to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# django-allauth config
SITE_ID = 1

# Authentication backend settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT = 'home'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
DEFAULT_FROM_EMAIL = 'admin@onlinebookstore.com'

# Media settings
""" Removed MEDIA_ROOT as django-storage will upload the files to s3"""
MEDIA_URL = '/media/'

# CELERY SETTINGS
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TIMEZONE = 'UTC'

# DJANGO STORAGE SETTINGS
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # replacing MEDIA_ROOT
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get('AWS_REGION')
AWS_DEFAULT_ACL = 'private'
# Do not overwrite files with the same name
AWS_S3_FILE_OVERWRITE = False
