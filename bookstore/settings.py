"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=61#-g)f8rhkpb-o+170b2r%eq6dz&0m53uek2&nzbpcink!dt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'social.apps.django_app.default',
    'registration',
    'bootstrap3',
    'bootstrap_themes',
    'compressor',
    'tastypie',
    'debug_toolbar',
    'store',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'bookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore.wsgi.application'

AUTHENTICATION_BACKENDS = (

        'social.backends.facebook.FacebookOAuth2',
        'django.contrib.auth.backends.ModelBackend',
)


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

#LANGUAGE_CODE = 'es-es'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
COMPRESS_ENABLED = True
STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = "/media/"

#Registration
ACCOUNT_ACTIVATION_DAYS=7
REGISTRATION_AUT_LOGIN= True
LOGIN_REDIRECT_URL = '/store/'
LOGIN_URL = '/accounts/login/'


#Email Settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_HOST_USER='postmaster@sandbox1f0e95517f454579b3c3e30fd183d97c.mailgun.org'
EMAIL_HOST_PASSWORD='2fdb06fb5d4380ba886f401b2c09d9e8'
EMAIL_PORT=587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'neapovea@gmail.com'



#social_auth facebook
SOCIAL_AUTH_FACEBOOK_KEY='1328408347238447'
SOCIAL_AUTH_FACEBOOK_SECRET='178cff3a5000519786c92df6fbb42b26'



DJANGO_LOG_LEVEL=DEBUG

#geip libraries
GEOIP_PATH= 'geo/'


LOGGING= {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(module)s | %(message)s'
                },
        },
    'handlers': {
        'file':{
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'basic',
            'maxBytes': 10000,
            'backupCount': 10,
            'filename': os.path.join(BASE_DIR, 'LOG_mystery_books.log'),
            },
        },
    'loggers': {
        'store': {
            'handlers': ['file'],
            'level': 'DEBUG',
            },
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            }
        }
    }