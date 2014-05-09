# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout, password_reset, password_reset_confirm, password_reset_done, password_change, password_reset_complete

urlpatterns = patterns('pro_tips.apps.accounts.views',
        ##PROFILE URLS
        url(r'^profile/$','user_profile',name='user-profile'),

        ## AUTH URLS
       url(r'^register/$', 'registration', name='register'),

       url(r'^login/$', login, {
            'template_name': 'user_profiles/sites/login.html'
        }, name='login'),

       url(r'^logout/$', logout, {
           'next_page': '/user-profiles/login/'
       }, name='logout'),

       url(r'^reset/$', password_reset, {
           #'template_name': 'profiles/sites/reset_password.html',
           'email_template_name': 'user_profiles/emails/reset_password.html',
           'post_reset_redirect': '/user-profiles/logout/'}, name='reset'),

       url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            password_reset_confirm,{
               'post_reset_redirect': '/user-profiles/login'
           },
            name='password_reset_confirm'),
       url(r'^reset/complete/$', password_reset_complete, {
           #'template_name': 'profiles/sites/reset_password.html',
            }, name='password_reset_complete'),

       url(r'^reset-done/?$', password_reset_done,name='password_reset_done'),

       url(r'^password_change/$', password_change, {
           'template_name': 'profiles/sites/change_password.html',
           'post_change_redirect': '/panel/logout/'},name='pwd-change'),


)