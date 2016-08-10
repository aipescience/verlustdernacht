from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from api import urls

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^impressum/$', TemplateView.as_view(template_name='impressum.html'), name='impressum'),
    url(r'^data/', TemplateView.as_view(template_name='data.html'), name='data'),
    url(r'^locations/$', TemplateView.as_view(template_name='locations.html'), name='locations'),
    url(r'^api/', include(urls)),
    url(r'^admin/', admin.site.urls),
]
