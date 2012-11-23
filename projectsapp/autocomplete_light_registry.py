#-*- coding:utf-8 -*-
from projectsapp.apps.members.models import Member
from projectsapp.apps.projects.models import Project

import autocomplete_light

autocomplete_light.register(Project,
    search_fields=('name',),
    autocomplete_js_attributes={'placeholder': 'Project...'}
)

autocomplete_light.register(Member, autocomplete_light.AutocompleteModelTemplate,
    autocomplete_template='autocomplete_template/member_autocomplete.html',
    search_fields=('name','trademark',),
    autocomplete_js_attributes={'placeholder': 'Member...'}
)