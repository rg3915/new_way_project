# -*- coding: utf-8 -*-
import io
import sys
import datetime
import names
import csv
from gen_random_values import *

ordered_list = []
repeat = 5000

with io.open('fixtures/pedidos.csv.json', 'wt') as f:
    for i in range(repeat):
        customer = random.randint(1, 200)
        vehicle = random.randint(1, 11)
        kit_optional = random.randint(1, 3)
        dealership_list = []
        for j in range(3):
            dealership = random.randint(1, 146)
            dealership_list.append((dealership))
        kiosk = random.randint(1, 287)
        status = random.choice(['c', 'p', 'a'])
        created_at = gen_timestamp(2015, 2015) + "+00"
        date = datetime.datetime.now().isoformat(" ") + "+00"
        ordered_list.append(
            (i + 1, kit_optional, kiosk, date, dealership_list, vehicle, status, created_at, customer))
    f.write('[\n')
    for l in ordered_list:
        s = "{\n" + \
            str('    "pk": ') + str(l[0]) + ",\n" + \
            str('    "model": "core.Ordered",\n') + \
            str('    "fields": {\n') + \
            str('        "kit_optional": ') + str(l[1]) + str(',\n') + \
            str('        "kiosk": ') + str(l[2]) + str(',\n') + \
            str('        "modified_at": "') + str(l[3]) + str('",\n') + \
            str('        "dealership": ') + str(l[4]) + str(',\n') + \
            str('        "vehicle": ') + str(l[5]) + str(',\n') + \
            str('        "status": "') + str(l[6]) + str('",\n') + \
            str('        "created_at": "') + str(l[7]) + str('",\n') + \
            str('        "customer": ') + str(l[8]) + str('\n') + \
            "    }\n"
        if l[0] == repeat:
            s = s + "}\n"
        else:
            s = s + "},\n"
        f.write(str(s))
    f.write(']')
