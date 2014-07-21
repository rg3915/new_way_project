# -*- coding: utf-8 -*-
from django.test import TestCase
from new_way.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):

    def test_form_has_fields(self):
        'Form must have 14 fields.'
        form = SubscriptionForm()
        self.assertItemsEqual(
            ['firstname', 'lastname', 'email', 'cpf', 'date_of_birth', 'phone', 'cell', 'address', 'complement',
                'district', 'city', 'uf', 'cep'], form.fields)

    def test_firstname_must_be_capitalized(self):
        'Firstname must be capitalized.'
        form = self.make_validated_form(firstname='REGIS')
        self.assertEqual('Regis', form.cleaned_data['firstname'])

    # def test_lastname_must_be_capitalized(self):
    #     'Lastname must be capitalized.'
    #     form = self.make_validated_form(lastname='da SILVA')
    #     self.assertEqual('da Silva', form.cleaned_data['lastname'])
