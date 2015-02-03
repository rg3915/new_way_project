from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from .models import Customer
from .forms import UserProfileForm


def home(request):
    return HttpResponse('Welcome')


class CustomerForm(CreateView):
    template_name = 'core/person/customer_form.html'
    model = Customer
    success_url = reverse_lazy('home')  # 'customer_list'


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/loggedin')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('core/person/profile.html', args)
