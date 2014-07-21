# -*- coding: utf-8 -*-
from django.test import TestCase
from new_way.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class DetailTest(TestCase):

    def setUp(self):
        s = Subscription.objects.create(
            firstname='Regis',
            lastname='da Silva',
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
            cep='04696000')
        self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))

    def test_get(self):
        'GET /inscricao/1/ should return status 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses template'
        self.assertTemplateUsed(
            self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context must have a subscription isinstance.'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was rendered.'
        self.assertContains(self.resp, 'Regis')


class DetailNotFound(TestCase):

    def test_not_found(self):
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)
