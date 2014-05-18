# -*- coding: utf-8 -*-
__author__ = 'wojtek'
from django.conf.urls import patterns, url, include
from django.contrib.auth.views import login, logout, password_reset, password_reset_confirm, password_reset_done, password_change, password_reset_complete

from pro_tips.apps.api import views

urlpatterns = patterns('pro_tips.apps.api.views',
        # unauthenticated urls
        url(r'^tips/$', views.TipsList.as_view(), name='tips_list'),
        url(r'^languages/$', views.LanguagesList.as_view(), name='languages_list'),
        url(r'^tip/comments/$', views.CommentsList.as_view(), name='comment_for_tip'),
        url(r'^tip/votes/(?P<tip>\d*)/$', views.get_votes_for_tip, name='votes_for_tip'),
        url(r'^comment/add/$', views.add_comment, name='add_comment'),
        #login required urls

        url(r'^tips/logged/$', views.TipsView.as_view(), name='tips_logged'),
        url(r'^tips/votes/logged/$', views.VotesView.as_view(), name='tips_votes'),
        url(r'^tip/favourites/logged/$', views.FavouriteView.as_view(), name='favourites_for_tip'),
        url(r'^languages/logged/$', views.LanguagesView.as_view(), name='languages_logged'),




)