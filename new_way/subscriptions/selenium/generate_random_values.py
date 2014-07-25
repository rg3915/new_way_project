# -*- coding: utf-8 -*-
import random
from datetime import *
"""
Gera valores randômicos para preenchimento do formulário 'inscrição'.
"""


def generate_cpf():
    return random.randint(00000000000, 99999999999)


def generate_date():
    year = random.randint(1960, 1996)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return str(year) + '-' + str(month) + '-' + str(day)


def generate_phone():
    number = random.randint(0000000000, 9999999999)
    return '(' + str(number)[:2] + ') ' + str(number)[2:6] + '-' + str(number)[6:]


def generate_cell():
    number = random.randint(00000000000, 99999999999)
    return '(' + str(number)[:2] + ') 9' + str(number)[2:6] + '-' + str(number)[6:]


def generate_cep():
    return random.randint(00000000, 99999999)
