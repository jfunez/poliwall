# Django settings for poliwall project.

from os.path import abspath, dirname, join, split
import sys

SETTINGS_ABSOLUTE_DIR = dirname(abspath(__file__))
PROJECT_PATH = split(SETTINGS_ABSOLUTE_DIR)[0]
sys.path.append(join(PROJECT_PATH, 'apps'))


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Juan Funez', 'juan.funez@gmail.com'),
    ('Juan Pablo Martinez', 'jpmea55@gmail.com'),
    ('Marcelo Ramos', 'marcelor@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'poliwal_prod',
        'USER': 'dbuser',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Montevideo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = PROJECT_PATH + '/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_PATH + '/static/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_PATH + '/poliwall/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^-2+-k=gsn23g=70d7i3g9^azeys+(t4&amp;9g^_k2g%3^dq2_s3!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'poliwall.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'poliwall.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'redactor',
    'bootstrap_admin',
    'django.contrib.admin',
    'poliwall',
    'south',
    'tastypie',
    'polidata',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# DJANGO-WYSIWYG-EDITOR Settings
if 'redactor' in INSTALLED_APPS:
    REDACTOR_OPTIONS = {'lang': 'en'}
    REDACTOR_UPLOAD = 'media/uploads/'

# DJANGO-LOCKDOWN ON/OFF
USE_LOCKDOWN = True  # change to False in localsettings if necessary

# LOCAL_SETTINGS
try:
    from local_settings import *
except ImportError:
    pass

# DJANGO-LOCKDOWN Settings
if USE_LOCKDOWN:
    MIDDLEWARE_CLASSES += ('lockdown.middleware.LockdownMiddleware',)
    INSTALLED_APPS += ('lockdown',)
    LOCKDOWN_URL_EXCEPTIONS = (
        r'^/admin/.*',
        r'^%s.*' % MEDIA_ROOT,
        r'^%s.*' % STATIC_ROOT,
        r'\.css$',
        r'\.js$',
    )
    LOCKDOWN_PASSWORDS = ('oximoron',)
    LOCKDOWN_FORM = 'lockdown.forms.AuthForm'
