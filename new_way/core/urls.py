# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'new_way.core.views',
    url(r'^$', 'home', name='home'),
)
