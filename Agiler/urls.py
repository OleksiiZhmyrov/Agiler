from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/ws100/retro/', include('retro.urls')),
    url(r'^api/ws100/core/', include('core.urls')),
    url(r'', include('ui.urls')),
)

urlpatterns += patterns(
    '',
    url(r'^api/ws100/auth/', include('rest_framework.urls', namespace='rest_framework')),
)
