# -*- coding: utf-8 -*-
from django.db import models

from projectsapp.apps.utils import nullable

class Member(models.Model):
    trademark = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128, **nullable)
    site = models.URLField(max_length=128, **nullable)
    contacts = models.TextField(**nullable)