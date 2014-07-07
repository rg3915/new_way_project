# -*- coding: utf-8 -*-
from django.db import models


class Subscription(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    cell = models.CharField(max_length=14)
    address = models.CharField(max_length=150)
    complement = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
