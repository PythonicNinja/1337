# -*- coding: utf-8 -*-
__author__ = 'wojtek'

from base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}