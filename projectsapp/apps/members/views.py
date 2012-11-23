# -*- coding: utf-8 -*-
from django.views.generic import UpdateView, CreateView, DetailView

from models import Member
from forms import MemberForm


class MemberMixin(object):
    model = Member

class MemberEditView(MemberMixin, UpdateView):
    form_class = MemberForm


class MemberCreateView(MemberMixin, CreateView):
    form_class = MemberForm

class MemberDetailView(DetailView):
    model = Member
