from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from api import urls

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^impressum$', TemplateView.as_view(template_name='impressum.html')),
    url(r'^data$', TemplateView.as_view(template_name='data.html')),
    url(r'^api/', include(urls)),
    url(r'^admin/', admin.site.urls),
)
