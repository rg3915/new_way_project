# -*- coding: utf-8 -*-
from django.test import TestCase
from new_way.subscriptions.forms import SubscriptionForm
from new_way.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class SubscribeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))

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
        self.assertContains(self.resp, 'type="text"', 12)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the subscriptio form.'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostTest(TestCase):

    def setUp(self):
        data = dict(
            firstname='Regis',
            lastname='Santos',
            cpf='11122233396',
            date_of_birth='1979-05-31',
            email='rg3915@yahoo.com.br',
            phone='11-2600-2500',
            cell='11-98700-0000',
            address=u'Avenida Engenheiro Eusébio Stevaux, 100',
            complement='Bloco A',
            district='Jurubatuba',
            city=u'São Paulo',
            uf='SP',
            cep='04696000'
        )
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Valid POST should redirect to /inscricao/1/'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'Valid POST must be saved.'
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):

    def setUp(self):
        data = dict(firstname='Regis',
                    lastname='Santos',
                    cpf='000000000012',
                    date_of_birth='1979-05-31',
                    email='rg3915@yahoo.com.br',
                    phone='11-2600-2500',
                    cell='11-98700-0000',
                    address=u'Avenida Engenheiro Eusebio Stevaux, 100',
                    complement='Bloco A',
                    district='Jurubatuba',
                    city=u'São Paulo',
                    uf='SP',
                    cep='04696000')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Invalid POST should not redirect.'
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        'Form must contain errors.'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Do not save data.'
        self.assertFalse(Subscription.objects.exists())
