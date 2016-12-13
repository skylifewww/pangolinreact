import os
import dj_database_url
from django.conf.global_settings import DATABASES

ATOMIC_REQUESTS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pangolinreact',
        'USER': 'skywww',
        'PASSWORD': 'skywww123',
        'HOST': u'127.0.0.1',
        'PORT': '',
    }
}

db_config = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_config)
if db_config:
    DATABASES['default'] =  db_config


# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/0',
#     },
#     'local': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'pangolin'
#     }
# }
