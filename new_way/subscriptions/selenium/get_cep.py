# -*- coding: utf-8 -*-
from cep import Correios
from generate_random_values import *
from list_cep import get_cep

# Não funciona
# n_cep = '04696000'
# n_cep = "%08i" % generate_cep()
# c = Correios()
# r = None

# while r is None:
#     try:
#         r = c.consulta(n_cep, primeiro=True)
#     except Exception, e:
#         raise e

# Escolhe um CEP válido em list_cep
cep = get_cep()
c = Correios()
r = c.consulta(cep, primeiro=True)
print -r['CEP']
print r['Logradouro']
print r
