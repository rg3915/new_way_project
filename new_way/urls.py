from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from new_way.core.views import *
from django.contrib import admin

urlpatterns = patterns(
    'new_way.core.views',
    url(r'^$', 'home', name='home'),

    url(r'^brands/$', BrandList.as_view(), name='brand_list'),
    url(r'^models/$', ModelList.as_view(), name='model_list'),
    url(r'^vehicles/$', VehicleList.as_view(), name='vehicle_list'),
    url(r'^vehicles/(?P<pk>\d+)/$',
        VehicleDetail.as_view(), name='vehicle_detail'),

    url(r'^dealerships/$', DealershipList.as_view(), name='dealership_list'),
    url(r'^stores/$', StoreList.as_view(), name='store_list'),
    url(r'^ordereds/$', OrderedList.as_view(), name='ordered_list'),

    url(r'^customer/add/$', CustomerCreate.as_view(), name='customer_add'),
    url(r'^ordered/add/$', OrderedCreate.as_view(), name='ordered_add'),

    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),

    # url(r'^about/$', 'about', name='about'),
    # url(r'^contact/$', 'contact', name='contact'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
