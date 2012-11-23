# -*- coding: utf-8 -*-
import os.path

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
import autocomplete_light

from projectsapp.apps.views import HomeView

#load autocomplete.
autocomplete_light.autodiscover()

admin.autodiscover()

static = os.path.join(os.path.dirname(__file__), 'static')

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^projects/', include('projectsapp.apps.projects.urls')),
    url(r'^members/', include('projectsapp.apps.members.urls')),
    #autocomplete
    url(r'autocomplete/', include('autocomplete_light.urls')),
    #Static
    (r'^static/(?P<path>.*)$','django.views.static.serve', {'document_root': static }),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )














