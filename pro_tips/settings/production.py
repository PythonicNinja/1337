from base import *

ALLOWED_HOSTS = ['*']

SECRET_KEY = "sekret"

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': 'pro_tips',
        'USER': 'pro_tips',
        'PASSWORD': '1',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}