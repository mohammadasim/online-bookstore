import socket

from .base import *

DEBUG = True

CURRENCY = '£'

ALLOWED_HOSTS = ["app"]

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# ************************** ALL AUTH CONFIGURATION ****************************** #
# Dev email settings, enables email output to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django debug toolbar settings
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + '1' for ip in ips]
INTERNAL_IPS = ['172.18.0.6']


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

# CELERY SETTINGS
CELERY_BROKER_URL = 'redis://redis:6379'
