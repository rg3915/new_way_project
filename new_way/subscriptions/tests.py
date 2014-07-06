# -*- coding: utf-8 -*-
from django.test import TestCase
from new_way.inscricoes.forms import InscricoesForm


class SubscribeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        'GET /inscricao/ retorna status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(
            self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 14)
        self.assertContains(self.resp, 'type="text"', 11)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the subscriptio form.'
        form = self.resp.context['form']
        self.assertIsInstance(form, InscricoesForm)

    def test_form_has_fields(self):
        'Form must have 12 fields.'
        form = self.resp.context['form']
        self.assertItemsEqual(
            ['firstname', 'lastname', 'email', 'cpf', 'dateofbirth', 'phone', 'cell', 'address',
                'district', 'city', 'state', 'cep'], form.fields)
