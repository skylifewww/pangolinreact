from settings.base import rel

STATIC_ROOT = rel('public', 'static')
MEDIA_ROOT = rel('public', 'media')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (rel('static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

IMAGE_UPLOAD_DIR = "img"
SESSION_SAVE_EVERY_REQUEST = True

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
        'toolbar': None,
        'toolbarCanCollapse': False,
        'forcePasteAsPlainText': True
    }
}

CKEDITOR_JQUERY_URL = 'static/pangolin/js/jquery-1.12.4.min.js'
