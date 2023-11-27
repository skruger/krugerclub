
import dj_database_url
from krugerclub.settings import *
import os

DEBUG = False
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(',')

DATABASES = {
    'default': dj_database_url.config(),
}

STATIC_URL = os.environ.get('STATIC_URL', '/static/')

WHITENOISE_ALLOW_ALL_ORIGINS = True
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
