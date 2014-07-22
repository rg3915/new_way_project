# -*- coding: utf-8 -*-
from django import forms
from new_way.subscriptions.models import Subscription
from django.utils.translation import ugettext as _
from django.template.defaultfilters import title


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription

    def clean_firstname(self):
        return title(self.cleaned_data['firstname'])

    def clean_lastname(self):
        return title(self.cleaned_data['lastname'])
