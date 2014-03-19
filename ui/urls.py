from django.conf.urls import patterns, url
from ui import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       url(r'^ui/$', views.render_template),
                       (r'^test/$', TemplateView.as_view(template_name='skeleton/temp/backbone_test.html')),
)
