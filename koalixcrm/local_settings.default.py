from settings import INSTALLED_APPS, MIDDLEWARE_CLASSES

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'koalixcrm',                      # Or path to database file if using sqlite3.
        'USER': 'koalixcrm',                      # Not used with sqlite3.
        'PASSWORD': 'koalix5crm1234',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if DEBUG:
    try:
        import debug_toolbar
        INTERNAL_IPS = ('127.0.0.1')
        DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
        MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
        INSTALLED_APPS += ('debug_toolbar',)
    except ImportError:
        pass
