# -*- coding: utf-8 -*-
from django.test import TestCase
from new_way.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):

    def test_form_has_fields(self):
        'Form must have 14 fields.'
        form = SubscriptionForm()
        self.assertItemsEqual(
            ['firstname', 'lastname', 'email', 'cpf', 'date_of_birth', 'phone', 'cell', 'address', 'complement',
                'district', 'city', 'state', 'cep'], form.fields)
