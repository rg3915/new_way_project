# -*- coding: utf-8 -*-
from django.shortcuts import render
from new_way.inscricoes.forms import InscricoesForm

def inscricao(request):
	return render(request, 'inscricoes/interessado_form.html', {'form': InscricoesForm()})
