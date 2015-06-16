import io
import sys
import datetime
import names
import csv
from gen_random_values import *

ordered_list = []
repeat = 15000

with io.open('fixtures/ordered_dealership.csv', 'wt') as f:
    f.write(
        u'id,ordered_id,dealership_id\n')
    i = 1
    while i < repeat:
        for o in range(1, 5001):
            for od in range(1, 4):
                d = random.randint(1, 146)
                ordered_list.append((i, o, d))
                i += 1
    for l in ordered_list:
        s = str(l[0]) + "," + str(l[1]) + "," + str(l[2]) + "\n"
        f.write(str(s))
