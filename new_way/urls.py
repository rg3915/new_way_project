from django.conf.urls import patterns, include, url
from new_way.core.views import *
from django.contrib import admin

urlpatterns = patterns(
    'new_way.core.views',
    url(r'^$', 'home', name='home'),

    url(r'^customers/$', CustomerList.as_view(), name='customer_list'),
    url(r'^dealerships/$', DealershipList.as_view(), name='dealership_list'),
    # url(r'^about/$', 'about', name='about'),
    # url(r'^contact/$', 'contact', name='contact'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
