# -*- coding: utf-8 -*-
__author__ = 'wojtek'
from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout, password_reset, password_reset_confirm, password_reset_done, password_change, password_reset_complete

from pro_tips.apps.api import views

urlpatterns = patterns('pro_tips.apps.api.views',

        url(r'^languages$', views.ListLanguages.as_view(), name='languages_list'),
        url(r'^tips$', views.ListTips.as_view(), name='tips'),
        url(r'^tip/comments/$', views.CommentsApiView.as_view(), name='comment_for_tip'),
)