# -*- coding: utf-8 -*-
from cep import Correios
from generate_random_values import *

# def get_cep(n_cep):
# n_cep = generate_cep()

# TODO encode

n_cep = '04696000'
c = Correios()
r = c.consulta(n_cep, primeiro=True)
print r['Logradouro']
print r['CEP']

# get_cep('04696000')
# lista = []
# lista.append(get_cep('04696000'))
# print lista
