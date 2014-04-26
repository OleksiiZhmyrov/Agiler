from django.conf.urls import patterns, include, url

from ui import views


urlpatterns = patterns(
    '',
    url(r'^$', views.redirect_home),
    url(r'^agiler/$', views.render_template),
    url(r'^agiler/help/', include('django.contrib.flatpages.urls')),
)
