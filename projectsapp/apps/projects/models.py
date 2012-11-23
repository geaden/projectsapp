# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from projectsapp.apps.members.models import Member
from projectsapp.apps.utils import nullable


class Project(models.Model):
    name = models.CharField(max_length=32)
    full_name = models.CharField(max_length=128)
    comment = models.TextField(blank=True)
    start_date = models.DateField()
    completion_date = models.DateField( **nullable)

    def get_absolute_url(self):
        return reverse('project-detail', (self.pk,))


class ProjectMember(models.Model):
    project = models.ForeignKey('projects.Project')
    member = models.ForeignKey('members.Member')