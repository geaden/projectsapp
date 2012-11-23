from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from views import MemberCreateView, MemberEditView, UserMemberListView, MemberDetailView

urlpatterns = patterns('',
    url(r'^edit/(?P<pk>\d+)/$',
        login_required(MemberEditView.as_view()),
        name='member-edit'),
    url(r'^add/$',
        login_required(MemberCreateView.as_view()),
        name='member-add'),
    url(r'^user/(?P<user_pk>\d+)/$',
        login_required(UserMemberListView.as_view()),
        name='user-member-list'),
    url(r'^(?P<pk>\d+)/$',
        login_required(MemberDetailView.as_view()),
        name='member-detail')
)
