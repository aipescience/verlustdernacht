from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

from api import urls

app_name = 'verlustdernacht'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('impressum/', TemplateView.as_view(template_name='impressum.html'), name='impressum'),
    path('daten/', TemplateView.as_view(template_name='data.html'), name='data'),
    path('standorte/', TemplateView.as_view(template_name='locations.html'), name='locations'),
    path('api/', include(urls)),
    path('admin/', admin.site.urls),
]
