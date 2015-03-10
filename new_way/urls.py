from django.conf.urls import patterns, include, url
from new_way.core.views import *
from django.contrib import admin

urlpatterns = patterns(
    'new_way.core.views',
    url(r'^$', 'home', name='home'),

    url(r'^brands/$', BrandList.as_view(), name='brand_list'),
    url(r'^models/$', ModelList.as_view(), name='model_list'),
    url(r'^vehicles/$', VehicleList.as_view(), name='vehicle_list'),
    url(r'^dealerships/$', DealershipList.as_view(), name='dealership_list'),
    # url(r'^about/$', 'about', name='about'),
    # url(r'^contact/$', 'contact', name='contact'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
