# -*- coding: utf-8 -*-
import os.path

from django.core.urlresolvers import reverse_lazy
from configurations import Settings


class BaseSettings(Settings):
    DEBUG = False

    TEMPLATE_DEBUG = DEBUG

    PROJECT_ROOT = os.path.split(os.path.abspath(__name__))[0]

    ADMINS = (
        # ('Your Name', 'your_email@example.com'),
    )

    AUTH_USER_MODEL = 'users.User'

    MANAGERS = ADMINS

    LOGIN_REDIRECT_URL = reverse_lazy('home')
    LOGIN_URL = reverse_lazy('login')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'projectsapp.db',
        }
    }

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # On Unix systems, a value of None will cause Django to use the same
    # timezone as the operating system.
    # If running in a Windows environment this must be set to the same as your
    # system time zone.
    TIME_ZONE = 'Europe/Moscow'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'ru'

    SITE_ID = 1

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = PROJECT_ROOT + '/media/'

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = '/media/'

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    STATIC_ROOT = PROJECT_ROOT + '/static/'

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'

    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(PROJECT_ROOT, 'projectsapp/templates/static'),
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = '6vyabh^unbhyx$(w30r1k2j31gghh-!nl(!2ll)e#y^n)1vme!'

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.core.context_processors.request',
        'django.contrib.auth.context_processors.auth',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    #    'django.middleware.csrf.CsrfResponseMiddleware'
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'projectsapp.urls'

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(PROJECT_ROOT, 'projectsapp/templates'),
    )

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django.contrib.comments',
        # 'django.contrib.admindocs',

        # 3rd-party apps
        'crispy_forms',
        'autocomplete_light',
        'south',
        'django_extensions',
        'sitetree',
        'django_nose',

        #projectsapp apps
        'projectsapp.apps.dictionaries',
        'projectsapp.apps.users',
        'projectsapp.apps.members',
        'projectsapp.apps.projects',
        'projectsapp.apps.wishes',
        'projectsapp.apps.works',
    )

    FIXTURE_DIRS = (
        os.path.join(PROJECT_ROOT, 'projectsapp/apps/dictionaries'),
        os.path.join(PROJECT_ROOT, 'projectsapp/apps/users'),
    )

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

#    SIMPLE_AUTOCOMPLETE_MODELS = ('factormatch.models.Member',)
#    SIMPLE_AUTOCOMPLETE = {'factormatch.models.Member': {'max_items': 10}}

    # See http://docs.djangoproject.com/en/dev/topics/logging
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

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    INTERNAL_IPS = ('127.0.0.1',)
