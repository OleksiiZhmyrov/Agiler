
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from retro import views

urlpatterns = patterns('',
                       url(r'^stickers/$', views.StickersList.as_view()),
                       url(r'^stickers/(?P<pk>[0-9]+)/$', views.StickerDetails.as_view()),
                       url(r'^boards/$', views.BoardsList.as_view()),
                       url(r'^boards/(?P<pk>[0-9]+)/$', views.BoardDetails.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
