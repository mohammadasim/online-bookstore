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
