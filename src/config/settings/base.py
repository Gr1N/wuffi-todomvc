# -*- coding: utf-8 -*-

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

####################
# DATABASE         #
####################

DATABASES = {
    'default': {
        'BACKEND': 'wuffi.core.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': 5432,
        'USER': None,
        'PASSWORD': None,
        'DATABASE': 'postgres',
        'POOLSIZE': 10,
    },
}

####################
# CACHE            #
####################

CACHES = {
    'default': {
        'BACKEND': 'wuffi.core.cache.backends.redis',
    },
}

###########
# LOGGING #
###########

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s %(message)s',
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'apps': {
            'handlers': ('console',),
            'level': 'DEBUG',
        },
    },
}

####################
# TEMPLATES        #
####################

TEMPLATES = {
    # 'DIRS': [
    #     'apps/todo/templates/',
    # ],
}
