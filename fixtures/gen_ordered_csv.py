# -*- coding: utf-8 -*-
import io
import sys
import datetime
import names
import csv
from gen_random_values import *

ordered_list = []
repeat = 5000

with io.open('fixtures/pedidos.csv', 'wt') as f:
    f.write(
        u'id,customer,vehicle,kit_optional,dealership,kiosk,status,created_at,modified_at\n')
    for i in range(repeat):
        customer = random.randint(1, 200)
        vehicle = random.randint(1, 11)
        kit_optional = random.randint(1, 3)
        dealership = random.randint(1, 146)
        kiosk = random.randint(1, 287)
        status = random.choice(['c', 'p', 'a'])
        created_at = gen_timestamp(2015, 2015) + "+00"
        date = datetime.datetime.now().isoformat(" ") + "+00"
        ordered_list.append(
            (i + 1, customer, vehicle, kit_optional, dealership, kiosk, status, created_at, date))
    for l in ordered_list:
        s = str(l[0]) + "," + str(l[1]) + "," + str(l[2]) + \
            "," + str(l[3]) + "," + str(l[4]) + "," + str(l[5]) + \
            "," + str(l[6]) + "," + str(l[7]) + "," + \
            str(l[8]) + "\n"
        f.write(str(s))
