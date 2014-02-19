
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = patterns('',
                       url(r'^teams/$', views.TeamsList.as_view()),
                       url(r'^teams/(?P<pk>[0-9]+)/$', views.TeamDetails.as_view()),
                       url(r'^sprints/$', views.SprintsList.as_view()),
                       url(r'^sprints/(?P<pk>[0-9]+)/$', views.SprintDetails.as_view()),
                       url(r'^users/$', views.UsersList.as_view()),
                       url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetails.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
