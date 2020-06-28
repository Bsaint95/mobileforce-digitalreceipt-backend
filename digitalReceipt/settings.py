"""
Django settings for digitalReceipt project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b&!_55_-n0p33)lx=#)$@h#9u13kxz%ucughc%k@w_^x0gyz!b'



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['frozen-island-67494.herokuapp.com','127.0.0.1','digital-receipt-07.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'authapp',
    'userManagement',
    'customers',
    'businessManagement.apps.BusinessmanagementConfig',
    'djoser',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'drf_yasg',
    "fcm_django"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'digitalReceipt.middleware.authMiddleWare.AuthorizationMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


ROOT_URLCONF = 'digitalReceipt.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'digitalReceipt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ddvfp9h9k873v4',
        'USER': 'hgdzjlhltufbsc',
        'PASSWORD': '51f8005b947bdbde56df87a760f18253999b1aca929fc0ab43c3869dd56335f7',
        'HOST': 'ec2-54-161-208-31.compute-1.amazonaws.com',
        'PORT': '5432',
}
}

import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)
#dj_database_url.config(default='postgres://...'}

REST_FRAMEWORK = {
    'DEFAULT AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.BasicAuthentication'
        'rest_framework.authentication.SessionAuthentication'
        'rest_framework.authentication.TokenAuthentication'

    ),
    'DEFAULT_PERMISSIONS-CLASSES':(
        'rest_framework.permissions.IsAuthenticated'
    ),

}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")


# No security issues occur in email the given password here is an app password
email_address = 'hngdigitalreceipt@gmail.com'
email_app_password = 'hosebgyqtuckqqkt'


FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": "AAAAMRXIXr0:APA91bGZWkJaJClsj91nx_wmwKyYYzl7BU287NjGVmKV7ZY5Xmxyt11ptjZZXtlaFvsuDRE3wXaOK6hWIcHd8hY93MXlwhcxI3U5Gz_u0zvOQ8g9VZzHBQI4Uef4CA3FRYY0OOEXzijL",
}

#Authentication backend (google Facebook and apple)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


SITE_ID = 1
LOGIN_REDIRECT_URL = 'logged/'