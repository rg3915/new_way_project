# -*- coding: utf-8 -*-
from cep import Correios
from generate_random_values import *
from list_cep import get_cep

# Escolhe um CEP válido em list_cep
cep = get_cep()
c = Correios()
r = c.consulta(cep, primeiro=True)
print r['CEP']
print r['Logradouro']
print r
