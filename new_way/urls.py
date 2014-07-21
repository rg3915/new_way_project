# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^inscricao/', include('new_way.subscriptions.urls', namespace='subscriptions')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('new_way.core.urls', namespace='core')),
)
