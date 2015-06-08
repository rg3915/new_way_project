import datetime
from datetime import date

'''
http://keyes.ie/calculate-age-with-python/
'''


def age(when, on=None):
    if on is None:
        on = datetime.date.today()
    was_earlier = (on.month, on.day) < (when.month, when.day)
    return on.year - when.year - (was_earlier)

age(date(2000, 1, 1))
