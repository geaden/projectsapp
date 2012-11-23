# -*- coding: utf-8 -*-
from django.db.models import Max
from django.views.generic import CreateView, UpdateView

from models import ProjectMember
from forms import ProjectMemberForm

class ProjectMemberCreateView(CreateView):
    model = ProjectMember
    form_class = ProjectMemberForm

  
class ProjectMemberUpdateView(UpdateView):
    model = ProjectMember
    form_class = ProjectMemberForm

