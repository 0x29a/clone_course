import os

from clone_course.settings.base import *

# IN-MEMORY TEST DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}
# END IN-MEMORY TEST DATABASE

OAUTH2_PROVIDER_URL = 'http://example.com/oauth2'
STUDIO_ROOT_URL = 'http://example.com/'