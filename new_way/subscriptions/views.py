# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from new_way.subscriptions.forms import SubscriptionForm
from new_way.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        form.full_clean()
        obj = Subscription(**form.cleaned_data)
        obj.save()
        return HttpResponseRedirect('inscricao/%d/' % obj.pk)
    else:
        return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})
