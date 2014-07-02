# -*- coding: utf-8 -*-
from django.test import TestCase
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
        self.resp = self.client.get('/')

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
