from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sistemaega',
        'USER': 'sistemaega',
        'PASSWORD': 'sistemaega',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = 'staticfiles'
MEDIA_URL = 'http://192.168.0.106:8000/media/'
MEDIA_ROOT = BASE_DIR.child('media')

#MANDRILL_API_KEY = "B7lPKBe39KmpXQTjtJF68g"