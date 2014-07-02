# -*- coding: utf-8 -*-
from django.test import TestCase


class InscricaoTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        'GET /inscricao/ retorna status code 200.'
        self.assertEqual(200, self.resp.status_code)
