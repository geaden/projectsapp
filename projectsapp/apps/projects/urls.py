# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from views import ProjectMemberCreateView

urlpatterns = patterns('',
    url(r'^join/$',
        ProjectMemberCreateView.as_view(),
        name = 'project-join'
    ),
)
