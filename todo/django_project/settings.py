"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from .custom_settings import (
    CUSTOM_INSTALLED_APPS,
    OWN_MIDDLEWARE,
    CORS_ALLOWED_ORIGINS,
    CSRF_TRUSTED_ORIGINS,
    STATIC_URL,
    OWN_ALLOWED_HOSTS,
    STATICFILES_DIRS,
    STATIC_ROOT,
    STATICFILES_STORAGE,
)
from pathlib import Path

import os  ### for environ

###
from environs import Env

env = Env()
env.read_env()
###

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-#c3p0z9+&vk@t0l&885_q8#p84t%*=hc4u7h9du%p_g$)2xs+)"
SECRET_KEY = env.str("SECRET_KEY_TODO", default=None)
# SECURITY WARNING: don't run with debug turned on in production!
### DEBUG = True
# DEBUG = "RENDER" not in os.environ
# DEBUG = os.environ.get("DEBUG_VALUE") is not None and os.environ.get("DEBUG_VALUE").lower() == "true"
DEBUG = env.bool("DEBUG_VALUE", default=False)

ALLOWED_HOSTS = []

ALLOWED_HOSTS += OWN_ALLOWED_HOSTS

### for render.com
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# INSTALLED_APPS.extend(CUSTOM_INSTALLED_APPS)
INSTALLED_APPS += CUSTOM_INSTALLED_APPS

# unrestricted access ### Added here
OWN_REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": {
        "rest_framework.permissions.AllowAny",
    }
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
MIDDLEWARE += OWN_MIDDLEWARE

CORS_ALLOWED_ORIGIN = CORS_ALLOWED_ORIGINS
CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

### STATIC_URL = "static/"
STATIC_URL = STATIC_URL

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STATICFILES_DIRS = STATICFILES_DIRS
STATIC_ROOT = STATIC_ROOT
STATICFILES_STORAGE = STATICFILES_STORAGE
