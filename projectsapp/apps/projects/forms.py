# -*- coding: utf-8 -*-
from django import forms

from models import ProjectMember

import autocomplete_light

class ProjectMemberForm(forms.ModelForm):
    class Meta:
        model = ProjectMember
        widgets = autocomplete_light.get_widgets_dict(ProjectMember)