# -*- coding: utf-8 -*-
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext as _
from django.contrib import admin
from new_way.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname',
                    'email', 'cpf', 'phone', 'cell', 'created_at', 'subcribed_today')
    date_hierarchy = 'created_at'
    search_fields = ('lastname', 'firstname',
                     'email', 'cpf', 'phone', 'cell', 'created_at')
    list_filter = ['created_at']

    def subcribed_today(self, obj):
        return obj.created_at.date() == datetime.today().date()

    subcribed_today.short_description = _(u'Inscrito hoje?')
    subcribed_today.boolean = True

admin.site.register(Subscription, SubscriptionAdmin)
