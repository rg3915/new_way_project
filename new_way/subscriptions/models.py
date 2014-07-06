# -*- coding: utf-8 -*-
from django.db import models


class Subscription(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cell = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    complement = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
