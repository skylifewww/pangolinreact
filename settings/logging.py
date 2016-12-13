from settings.base import rel

LOG_FILE = rel('logs', 'app.log')
LOG_FILE_SIZE = 1024 * 1024 * 16  # bytes
LOG_FILE_BACKUP_COUNT = 10

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'complete': {
            'format': '%(levelname)s:%(asctime)s:%(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s:%(asctime)s: %(message)s'
        },
        'null': {
            'format': '%(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'complete'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE,
            'maxBytes': LOG_FILE_SIZE,
            'backupCount': LOG_FILE_BACKUP_COUNT,
            'formatter': 'complete'}
    },
    'loggers': {
        'django': {
            'handlers': ['logfile', 'console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.request': {
            'handlers': ['logfile', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'pangolin': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}
