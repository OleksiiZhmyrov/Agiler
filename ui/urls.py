from django.conf.urls import patterns, url
from ui import views

urlpatterns = patterns('',
                       url(r'^ui/$', views.render_template),
)
