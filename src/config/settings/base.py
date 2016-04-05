# -*- coding: utf-8 -*-

####################
# CACHE            #
####################

CACHES = {
    'default': {
        'BACKEND': 'wuffi.core.cache.backends.redis',
    },
}
