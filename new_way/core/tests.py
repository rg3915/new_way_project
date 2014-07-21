# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse as r
"""
Usando um assert por método de test.
Teste de Request e Response.
"""


class HomeTest(TestCase):

    def setUp(self):
        """
        Nome especial de método do Python, roda sempre antes de cada teste.
        Armazena a resposta da requisição.
        """
        self.resp = self.client.get(r('core:home'))

    def test_get(self):
        """
        GET /retorna o status code 200, sucesso.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Página usada no template index.html
        """
        self.assertTemplateUsed(self.resp, 'index.html')
