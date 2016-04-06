# -*- coding: utf-8 -*-

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
