from django.conf.urls import patterns, url

from ui import views


urlpatterns = patterns(
    '',
    url(r'^$', views.redirect_home),
    url(r'^agiler/$', views.render_template),
)
