# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
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

    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError(
                _(u'Informe seu e-mail ou telefone ou celular.'))

        return self.cleaned_data
