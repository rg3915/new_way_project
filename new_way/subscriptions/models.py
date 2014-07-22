# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    firstname = models.CharField(_('nome'), max_length=100)
    lastname = models.CharField(_('sobrenome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    date_of_birth = models.DateField(_('data de nascimento'), )
    email = models.EmailField(_('email'), unique=True)
    phone = models.CharField(_('telefone'), max_length=14)
    cell = models.CharField(_('celular'), max_length=14)
    address = models.CharField(_(u'endereço'), max_length=150)
    complement = models.CharField(_('complemento'), max_length=100, blank=True)
    district = models.CharField(_('bairro'), max_length=100)
    city = models.CharField(_('cidade'), max_length=100)
    uf = models.CharField(_('UF'), max_length=100)
    cep = models.CharField(_('CEP'), max_length=8)
    created_at = models.DateTimeField(_('criado em'), auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = _(u'inscrição')
        verbose_name_plural = _(u'inscrições')

    def __unicode__(self):
        return self.lastname + ', ' + self.firstname
