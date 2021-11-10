from pathlib import Path

import config

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config.config('secret_key')
DEBUG = True

ALLOWED_HOSTS = []



ROOT_URLCONF = 'chamada_eletronica.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chamada_eletronica.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS = [
    'web.apps.WebConfig',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Belem'

USE_TZ = False

USE_I18N = True

USE_L10N = True



STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
