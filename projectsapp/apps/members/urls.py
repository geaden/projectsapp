from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from views import MemberCreateView, MemberEditView, MemberDetailView

urlpatterns = patterns('',
    url(r'^edit/(?P<pk>\d+)/$',
        MemberEditView.as_view(),
        name='member-edit'),
    url(r'^add/$',
        MemberCreateView.as_view(),
        name='member-add'),
    url(r'^(?P<pk>\d+)/$',
        MemberDetailView.as_view(),
        name='member-detail')
)
