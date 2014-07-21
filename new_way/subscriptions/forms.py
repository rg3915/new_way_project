# -*- coding: utf-8 -*-
from django import forms
from new_way.subscriptions.models import Subscription
from django.utils.translation import ugettext as _


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription

    def clean_firstname(self):
        firstname = self.cleaned_data['firstname']
        words = map(lambda w: w.capitalize(), firstname.split())
        capitalized_name = ' '.join(words)
        return capitalized_name

    def clean_lastname(self):
        lastname = self.cleaned_data['lastname']
        words = map(lambda w: w.capitalize(), lastname.split())
        capitalized_name = ' '.join(words)
        return capitalized_name
