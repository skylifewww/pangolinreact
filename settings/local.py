from settings import DEVELOPMENT, INSTALLED_APPS, MIDDLEWARE_CLASSES

DOMAIN = 'localhost:8000'
ALLOWED_HOSTS = ['localhost']

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'skylifewww@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'skylifewww@gmail.com'
EMAIL_HOST_PASSWORD = 'skywww123'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_PORT = 587

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pangolinreact',
        'USER': 'skywww',
        'PASSWORD': 'skywww123',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# if DEVELOPMENT:
#     # debug toolbar settings
#     INTERNAL_IPS = ('127.0.0.1',)
#     DEBUG_TOOLBAR_PATCH_SETTINGS = False
#     INSTALLED_APPS += ('debug_toolbar',)
#     MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
