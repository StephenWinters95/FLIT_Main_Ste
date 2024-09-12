"""
Django settings for django_financial_planner project.

Generated by 'django-admin startproject' using Django 3.2.22.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from django.contrib.messages import constants as messages
if os.path.isfile("env.py"):
        import env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DMcC 21/11/23 set to True to try deployed version of Heroku app
DEBUG = True
# DEBUG = False

# DMcC 20/11/23 Taggit caused uninstall of Djg 3.X, fresh install of Django 4
# Below is to overcome resulting CSRF errors on the site's admin page
CSRF_TRUSTED_ORIGINS = [
    'https://8000-deemccart-cipp4financia-vv93ot4q6wj.ws-eu106.gitpod.io',
    'https://financial-planner-6a030328a9ac.herokuapp.com/',
    'https://flit-e60c994ef0ea.herokuapp.com',
    'https://8000-deemccart-flitfpmerge-uuv2t1vze42.ws-eu115.gitpod.io',
    'https://8000-deemccart-flitfpmerge-4jnbvxtlp9z.ws-eu116.gitpod.io',
    os.environ.get("CSRF_TRUSTED_ORIGINS"),
    ]


ALLOWED_HOSTS = ['8000-deemccart-cipp4financia-vv93ot4q6wj.ws-eu105.gitpod.io',
                 '8000-deemccart-cipp4financia-vv93ot4q6wj.ws-eu106.gitpod.io',
                 'financial-planner-6a030328a9ac.herokuapp.com',
                 '8000-deemccart-flitfpmerge-uuv2t1vze42.ws-eu115.gitpod.io',
                 'flit-e60c994ef0ea.herokuapp.com',
                 '8000-deemccart-flitfpmerge-4jnbvxtlp9z.ws-eu116.gitpod.io',
                 os.environ.get("ALLOWED_HOSTS"),
                 
                 ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'django_summernote',
    'crispy_forms',
    'fp_blog',
    'fp_personal',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'taggit',
    ]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO:  'alert-info',
    messages.SUCCESS:  'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
    }

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'django_financial_planner.urls'

ACCOUNT_EMAIL_VERIFICATION = 'none'

# DMcC 21/11/23 this option added to test out deployed Heroku version"
# Auto deploy now deactivated so option commented out 21/11 after manual deploy
XFRAME_OPTIONS = 'SAMEORIGIN'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'django_financial_planner.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DMcC 19/08/24 uncommented as want to use local database for coding so I can build migrations 
# DMcC 09/09/24 commented out as want to try new database instance on ElephantSQL (initially)
# DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.sqlite3',
#       'NAME': BASE_DIR / 'db.sqlite3',
#   }
#}

# DMcC 19/08/24 commented out as want to use local database for coding
DATABASES = {
  'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
           }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
print('Staticfiles_dirs value is', STATICFILES_DIRS)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
print('STATIC_ROOT is', STATIC_ROOT)
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
