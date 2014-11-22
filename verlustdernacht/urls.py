from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'verlustdernacht.views.index'),
    url(r'^impressum$', 'verlustdernacht.views.impressum'),
)
