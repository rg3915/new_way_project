# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _


class SubscriptionForm(forms.Form):
    firstname = forms.CharField(label=_('Nome'))
    lastname = forms.CharField(label=_('Sobrenome'))
    cpf = forms.CharField(label=_('CPF'))
    date_of_birth = forms.CharField(label=_('Data de Nascimento'))
    email = forms.EmailField(label=_('Email'))
    phone = forms.CharField(label=_('Telefone'))
    cell = forms.CharField(label=_('Celular'))
    address = forms.CharField(label=_(u'Endereço'))
    complement = forms.CharField(label=_('Complemento'))
    district = forms.CharField(label=_('Bairro'))
    city = forms.CharField(label=_('Cidade'))
    state = forms.CharField(label=_('UF'))
    cep = forms.CharField(label=_('CEP'))
    #created_at = forms.DateTimeField(label=_('criado em'), auto_now_add=True)
