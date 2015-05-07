# -*- coding: utf-8 -*-
import io
import sys
import datetime
import names
import csv
from gen_random_values import *

""" List of values for use in choices in models. """
person_list = []
repeat = 101

# last_login datetime

with io.open('fixtures/usuarios.csv', 'wt') as f:
    f.write(
        u'id,password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined\n')
    for i in range(1, repeat):
        g = random.choice(['M', 'F'])
        if g == 'M':
            first_name = names.get_first_name(gender='male')
        else:
            first_name = names.get_first_name(gender='female')
        last_name = names.get_last_name()
        username = first_name.lower() + '.' + last_name.lower()
        password = first_name.lower()
        email = first_name[
            0].lower() + '.' + last_name.lower() + '@example.com'
        date = datetime.datetime.now().isoformat(" ") + "+00"
        person_list.append(
            (i + 1, password, date, 'False', username, first_name, last_name, email, 'True', 'True', date))
    for l in person_list:
        s = str(l[0]) + "," + str(l[1]) + "," + str(l[2]) + \
            "," + str(l[3]) + "," + str(l[4]) + "," + str(l[5]) + \
            "," + str(l[6]) + "," + str(l[7]) + "," + str(l[8]) + \
            "," + str(l[9]) + "," + str(l[10]) + "\n"
        f.write(str(s))
