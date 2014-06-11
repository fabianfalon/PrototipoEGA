from unipath import Path
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
	   'south',

	)

LOCAL_APPS = (
		'apps.alumno',
		'apps.bedel',
				
			
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


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = 'http://localhost:8000/media/'

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'alumno.User'