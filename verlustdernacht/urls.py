from django.conf.urls import patterns, include, url

from lmdb import urls

urlpatterns = patterns('',
    url(r'^$', 'verlustdernacht.views.index'),
    url(r'^impressum$', 'verlustdernacht.views.impressum'),
    url(r'^api/', include(urls)),
)
