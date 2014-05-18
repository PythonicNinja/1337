from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^', include('pro_tips.apps.main_sites.urls') , name='home'),

    url(r'^accounts/', include('pro_tips.apps.accounts.urls', namespace="accounts")),
    url(r'^api/', include('pro_tips.apps.api.urls', namespace="api")),

    #include django-admin urls
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),


    #Third-party apps urls
    url(r'', include('social_auth.urls')),
    url(r'^front-edit/', include('front.urls')),
)

from django.conf import settings
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
