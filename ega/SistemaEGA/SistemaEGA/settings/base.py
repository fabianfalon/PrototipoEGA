from .email_info import EMAIL_USE_TLS, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT
from unipath import Path

EMAIL_USE_TLS= EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT


BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = '98_x--00^13)h%6td6%5o70&d6su-014$31xo*hr84pji8t3i3'

DJANGO_APPS = (
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
		)

THIRD_PARTY_APPS = (
	   #'south',
	   'djrill',
	   'wkhtmltopdf',
	   #'sorl.thumbnail',

	)

LOCAL_APPS = (
		'apps.alumno',
		'apps.home',
				
			
  )

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SistemaEGA.urls'

WSGI_APPLICATION = 'SistemaEGA.wsgi.application'

LANGUAGE_CODE = 'es-AR'


TIME_ZONE = 'America/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = 'http://192.168.0.105::8000/media/'

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'alumno.User'

WKHTMLTOPDF_CMD_OPTIONS = {
   'encoding':'utf8',
   'quiet':True,
}

#EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"


