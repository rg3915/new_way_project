# -*- coding: utf-8 -*-
from django.test import TestCase
from new_way.subscriptions.models import Subscription

class DetailTest(TestCase):
	def setUp(self):
		s = Subscriptions.objects.create(firstname='Regis',
            lastname='Santos',
            cpf='00000000012',
            date_of_birth='1979-05-31',
            email='rg3915@yahoo.com.br',
            phone='11-2600-2500',
            cell='11-98700-0000',
            address='Avenida Engenheiro Eusébio Stevaux, 100',
            complement='Bloco A',
            district='Jurubatuba',
            city='São Paulo',
            uf='SP',
            cep='04696-000')
		self.resp = self.client.get('/inscricao/%d/' % s.pk)

	def test_get(self):
		'GET /inscricao/1/ should return status 200.'
		self.assertEquals(200, resp.status_code)

	def test_template(self):
		'Uses template'
		self.assertTemplateUsed(self.resp,
		'subscriptions/subscription_detail.html')

	def test_context(self):
		'Context must have a subscription isinstance.'
		subscripton = self.resp.context['subscripton']
		self.assertIsInstance(subscripton, Subscription)

	def test_html(self):
		'Check if subscription data was rendered.'
		self.assertContains(self.resp, 'Regis')

class DetailNotFound(TestCase):
	def test_not_found(self):
		response = self.client.get('/inscricao/0/')
		self.assertEquals(404, response.status_code)		