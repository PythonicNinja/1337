# -*- coding: utf-8 -*-
__author__ = 'wojtek'
from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout, password_reset, password_reset_confirm, password_reset_done, password_change, password_reset_complete

from pro_tips.apps.api import views

urlpatterns = patterns('pro_tips.apps.api.views',
        # unauthenticated urls
        url(r'^tips/$', views.TipsList.as_view(), name='tips_list'),
        url(r'^languages/$', views.LanguagesList.as_view(), name='languages_list'),
        url(r'^tip/comments/$', views.CommentsList.as_view(), name='comment_for_tip'),

        #login required urls
        url(r'^tips/logged/$', views.TipsView.as_view(), name='tips_logged'),
        url(r'^languages/logged/$', views.LanguagesView.as_view(), name='languages_logged'),




)