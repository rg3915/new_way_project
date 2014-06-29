from django.conf.urls import patterns, include, url
from core.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'new_way.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
