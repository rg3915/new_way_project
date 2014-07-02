from django.conf.urls import patterns, include, url
from core.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'new_way.core.views.home', name='home'),
    url(r'^inscricao/$',
        'new_way.inscricao.views.inscricao', name='inscricao'),
    url(r'^admin/', include(admin.site.urls)),
)
