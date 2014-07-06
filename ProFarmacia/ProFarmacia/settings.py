"""
Django settings for ProFarmacia project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUTA_PROYECTO=os.path.dirname(os.path.realpath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a=7u4icv(t0tr7ybzr39==i=7ub!b6l&ba#=aat#0drl&jbmt5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ProFarmacia.apps.regfarmacia',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ProFarmacia.urls'

WSGI_APPLICATION = 'ProFarmacia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'globalF',
        'USER':'root',
        'PASSWORD':'',

    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-bo'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
###################################################
#Aqui va la configuracion para el envio de correo electronico
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER = 'darkdragonplec@gmail.com'
EMAIL_HOST_PASSWORD='zerowolfus'
EMAIL_USE_TLS=True
###################################################

STATIC_URL = '/static/'
TEMPLATE_DIRS=(os.path.join(RUTA_PROYECTO,"template"),)
STATICFILES_DIRS=(os.path.join(RUTA_PROYECTO,"static"),)
MEDIA_ROOT=os.path.join(BASE_DIR,'ProFarmacia/media')