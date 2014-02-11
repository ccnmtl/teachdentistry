# flake8: noqa
from settings_shared import *

TEMPLATE_DIRS = (
    "/var/www/teachdentistry/teachdentistry/teachdentistry/templates",
)

MEDIA_ROOT = '/var/www/teachdentistry/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', '/var/www/teachdentistry/teachdentistry/sitemedia'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'teachdentistry',
        'HOST': '',
        'PORT': 6432,
        'USER': '',
        'PASSWORD': '',
    }
}

COMPRESS_ROOT = "/var/www/teachdentistry/teachdentistry/media/"
DEBUG = False
TEMPLATE_DEBUG = DEBUG

if 'migrate' not in sys.argv:
    INSTALLED_APPS.append('raven.contrib.django.raven_compat')

try:
    from local_settings import *
except ImportError:
    pass
