from django.conf.urls import patterns, include, url
from new_way.core.views import *
from django.contrib import admin

urlpatterns = patterns(
    'new_way.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^customer/add', CustomerForm.as_view(), name='customer_form'),
    url(r'^profile/add', 'user_profile', name='userprofile_form'),
    url(r'^admin/', include(admin.site.urls)),
)
