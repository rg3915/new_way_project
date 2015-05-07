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
user_list = []
repeat = 100

''' Lendo os dados de enderecos_.csv '''
with open('fixtures/enderecos_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

''' Lendo os dados de usuarios.csv '''
with open('fixtures/usuarios.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        user_list.append(dct)
    f.close()

with io.open('fixtures/funcionarios.csv', 'wt') as f:
    f.write(
        u'id,user,gender,first_name,last_name,cpf,birthday,email,phone,cell,address,address_number,district,city,uf,cep,occupation,dealership,comissioned,comission,created_at,modified_at\n')
    for i in range(1, repeat):
        g = random.choice(['M', 'F'])
        user = user_list[i]['id']
        first_name = user_list[i]['first_name']
        last_name = user_list[i]['last_name']
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
        occupation = random.randint(1, 4)
        dealership = random.randint(1, 6)
        comissioned = random.choice([True, False])
        comission = 0.01
        date = datetime.datetime.now().isoformat(" ") + "+00"
        person_list.append(
            (i + 1, user, g, first_name, last_name, cpf, birthday, email, phone, cell, address, address_number, district, city, uf, cep, occupation, dealership, comissioned, comission, date, date))
    for l in person_list:
        s = str(l[0]) + "," + str(l[1]) + "," + str(l[2]) + \
            "," + str(l[3]) + "," + str(l[4]) + "," + str(l[5]) + \
            "," + str(l[6]) + "," + str(l[7]) + "," + str(l[8]) + \
            "," + str(l[9]) + "," + str(l[10]) + "," + str(l[11]) + \
            "," + str(l[12]) + "," + str(l[13]) + "," + str(l[14]) + \
            "," + str(l[15]) + "," + str(l[16]) + "," + str(l[17]) + \
            "," + str(l[18]) + "," + str(l[19]) + "," + str(l[20]) + \
            "," + str(l[21]) + "\n"
        f.write(str(s))
