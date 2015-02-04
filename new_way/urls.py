from django.conf.urls import patterns, include, url
from new_way.core.views import *
from django.contrib import admin

urlpatterns = patterns(
    'new_way.core.views',
    url(r'^$', 'home', name='home'),

    # url(r'^download/$', 'download', name='download'),
    # url(r'^about/$', 'about', name='about'),
    # url(r'^contact/$', 'contact', name='contact'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
