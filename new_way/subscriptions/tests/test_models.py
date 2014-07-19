# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from new_way.subscriptions.models import Subscription


class SubscriptionTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
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
        # CPF válido: 33322211169, 55566678963

    def test_create(self):
        """
        Subscription must have firstname, lastname, cpf, date_of_birth, email,
        phone, cell, address, complement, district, city, uf, cep
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Santos', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):

    def setUp(self):
        # Create a first entry to force the collision
        Subscription.objects.create(
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

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(
            firstname='Regis',
            lastname='Santos',
            cpf='11122233396',
            date_of_birth='1979-05-31',
            email='regis@yahoo.com.br',
            phone='11-2600-2500',
            cell='11-98700-0000',
            address=u'Avenida Engenheiro Eusébio Stevaux, 100',
            complement='Bloco A',
            district='Jurubatuba',
            city=u'São Paulo',
            uf='SP',
            cep='04696000'
        )
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(
            firstname='Regis',
            lastname='Santos',
            cpf='33322211169',
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
        self.assertRaises(IntegrityError, s.save)
