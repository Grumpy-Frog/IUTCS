"""
Django settings for IUTCS project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

import os

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = []

# For MARKDOWN Options
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Application definition


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mdeditor",
    "blogs",
    "achievements",
    "admin_panel",
    "activity",
    "sweetify",
    "participated_team",
    "intra_university_event",
    "inter_university_event",
    'bootstrap3',
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "IUT_CS.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = "IUT_CS.wsgi.application"

# possible options: 'sweetalert', 'sweetalert2' - default is 'sweetalert2'
SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'

LOGIN_REDIRECT_URL = 'admin_panel'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


IS_LOCALHOST = 3

if IS_LOCALHOST == 1:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),  # or the hostname where your MySQL server is running
            'PORT': '3306',  # or the port on which your MySQL server is listening
        }
    }
elif IS_LOCALHOST == 2:

    import dj_database_url

    # postgres://iutcs_user:ylJkVP0TO9wG6n38kYQT7JI9xLuej3TK@dpg-cka726mv3ddc73bjib50-a.oregon-postgres.render.com/iutcs

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',  # or the hostname where your PostgreSQL server is running
            'PORT': '',  # or the port on which your PostgreSQL server is listening
        }
    }

    dabase_url = os.environ.get("DATABASE_URL")

    DATABASES["default"] = dj_database_url.parse(dabase_url)

    DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

    SECRET_KEY = os.environ.get("SECRET_KEY")

else:
    import dj_database_url

    # postgres://iutcs_user:ylJkVP0TO9wG6n38kYQT7JI9xLuej3TK@dpg-cka726mv3ddc73bjib50-a.oregon-postgres.render.com/iutcs

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',  # or the hostname where your PostgreSQL server is running
            'PORT': '',  # or the port on which your PostgreSQL server is listening
        }
    }

    DATABASES["default"] = dj_database_url.parse(
        "postgres://iutcs_h3of_user:HX8qhsCXoQ4Y1Jag9eEKQSu4pj2reXYq@dpg-cmkdm2da73kc73blcvlg-a.oregon-postgres.render.com/iutcs_h3of")

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),  # or the hostname where your MySQL server is running
        'PORT': '3306',  # or the port on which your MySQL server is listening
    }
}
'''

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
if IS_LOCALHOST==2:
    STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MDEDITOR_CONFIGS = {
    'default': {
        'width': '90% ',  # Custom edit box width
        'height': 500,  # Custom edit box height
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],  # custom edit box toolbar
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # image upload format type
        'image_folder': 'editor',  # image save the folder name
        'theme': 'default',  # edit box theme, dark / default
        'preview_theme': 'default',  # Preview area theme, dark / default
        'editor_theme': 'default',  # edit area theme, pastel-on-dark / default
        'toolbar_autofixed': True,  # Whether the toolbar capitals
        'search_replace': True,  # Whether to open the search for replacement
        'emoji': True,  # whether to open the expression function
        'tex': True,  # whether to open the tex chart function
        'flow_chart': True,  # whether to open the flow chart function
        'sequence': True,  # Whether to open the sequence diagram function
        'watch': True,  # Live preview
        'lineWrapping': False,  # lineWrapping
        'lineNumbers': False,  # lineNumbers
        'language': 'en'  # zh / en / es
    }

}


# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'testemail21212@gmail.com'
EMAIL_HOST_PASSWORD = 'uyam fstf qpzj imbs'
DEFAULT_FROM_EMAIL = 'testemail21212@gmail.com'
