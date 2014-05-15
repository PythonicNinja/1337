# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout, password_reset, password_reset_confirm, password_reset_done, password_change, password_reset_complete

urlpatterns = patterns('pro_tips.apps.main_sites.views',
        url(r'^$', 'index', name='index'),
        url(r'^home/$', 'index', name='index'),
        url(r'^tips/$', 'tips', name='tips'),

)