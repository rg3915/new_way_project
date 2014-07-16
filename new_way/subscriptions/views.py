# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from new_way.subscriptions.forms import SubscriptionForm
from new_way.subscriptions.models import Subscription

# def subscribe(request):
# 	if request.method == 'POST':
# 		form = SubscriptionForm(request.POST)
# 		if form.is_valid():
# 			obj = Subscription(**form.cleaned_data)
# 			obj.save()
# # No slide 207 é substituida a linha 11 e 12 de views por
# 			# obj = form.save()

# 			return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
# 		else:
# 			return render(request, 'subscriptions/subscription_form.html',
# 				{'form': form})
# 	else:
# 		return render(request, 'subscriptions/subscription_form.html',
# 			{'form': SubscriptionForm()})

def subscribe(request):
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)

def new(request):
	return render(request, 'subscriptions/subscription_form.html',
		{'form': SubscriptionForm()})

def create(request):
	form = SubscriptionForm(request.POST)
	if not form.is_valid():
		return render(request, 'subscriptions/subscription_form.html',
			{'form': form})

	obj = form.save()
	return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
