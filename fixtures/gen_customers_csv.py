# -*- coding: utf-8 -*-
import io
import sys
import datetime
import names
import csv
from gen_random_values import *

""" List of values for use in choices in models. """
person_list = []
address_list = []
repeat = 200

''' Lendo os dados de enderecos_.csv '''
with open('fixtures/enderecos_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

with io.open('fixtures/clientes.csv', 'wt') as f:
    f.write(
        u'id,gender,first_name,last_name,cpf,birthday,email,phone,cell,address,address_number,district,city,uf,cep,created_at,modified_at\n')
    for i in range(repeat):
        g = random.choice(['M', 'F'])
        if g == 'M':
            first_name = names.get_first_name(gender='male')
        else:
            first_name = names.get_first_name(gender='female')
        last_name = names.get_last_name()
        cpf = gen_doc()
        birthday = gen_date()
        email = first_name[
            0].lower() + '.' + last_name.lower() + '@example.com'
        phone = gen_phone()
        cell = gen_phone()
        n = random.randint(1, 5)  # escolhe um id de enderecos_.csv
        address = address_list[n]['address']
        address_number = address_list[n]['address_number']
        district = address_list[n]['district']
        city = address_list[n]['city']
        uf = address_list[n]['uf']
        cep = address_list[n]['cep']
        date = datetime.datetime.now().isoformat(" ") + "+00"
        person_list.append(
            (i + 1, g, first_name, last_name, cpf, birthday, email, phone, cell, address, address_number, district, city, uf, cep, date, date))
    for l in person_list:
        s = str(l[0]) + "," + str(l[1]) + "," + str(l[2]) + \
            "," + str(l[3]) + "," + str(l[4]) + "," + str(l[5]) + \
            "," + str(l[6]) + "," + str(l[7]) + "," + str(l[8]) + \
            "," + str(l[9]) + "," + str(l[10]) + "," + str(l[11]) + \
            "," + str(l[12]) + "," + str(l[13]) + "," + str(l[14]) + \
            "," + str(l[15]) + \
            "," + str(l[16]) + "\n"
        f.write(str(s))
