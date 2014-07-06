# -*- coding: utf-8 -*-
from django.test import TestCase
from new_way.subscriptions.models import Subscription


class SubscriptionTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            firstname='Regis',
            lastname='Santos',
            # CPF válido: 33322211169, 55566678963
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
            cep='04696-000'
        )

    def test_create(self):
        """
        Subscription must have firstname, lastname, cpf, date_of_birth, email,
        phone, cell, address, complement, district, city, uf, cep
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)
