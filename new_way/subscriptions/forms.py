# -*- coding: utf-8 -*-
from django import forms
from new_way.subscriptions.models import Subscription
from django.utils.translation import ugettext as _


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
