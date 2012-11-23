# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.shortcuts import redirect

from exeviks.apps.projects.models import Project, Factor


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('user-detail', request.user.pk)
        return super(HomeView, self).get(request)