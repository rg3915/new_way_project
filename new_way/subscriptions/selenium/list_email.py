# -*- coding: utf-8 -*-
import random


def get_email():
    list_email = [
        '@email.com',
        '@imail.com',
        '@example.com',
        '@newway.com',
        '@nw.com',
    ]
    email = random.choice(list_email)
    return email
