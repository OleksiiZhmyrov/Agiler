from django.conf.urls.static import static
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from retro import views
from Agiler import settings

urlpatterns = patterns('',
                       url(r'^stickers/$', views.StickersList.as_view()),
                       url(r'^stickers/(?P<pk>[0-9]+)/$', views.StickerDetails.as_view()),
                       url(r'^boards/$', views.BoardsList.as_view()),
                       url(r'^boards2/(?P<pk>[0-9]+)/$', views.BoardDetails.as_view()),
                       url(r'^boards/(?P<pk>[0-9]+)/$', views.BoardDetailsContainer.as_view()),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
