from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from .models import Customer, Dealership, Address, Brand, Modell, Vehicle, Store
from .forms import CustomerForm


def home(request):
    return render(request, 'index.html')


class CustomerForm(CreateView):
    template_name = 'core/person/customer_create_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('home')  # 'customer_list'


class BrandList(ListView):
    template_name = 'core/vehicle/brand_list.html'
    model = Brand


class ModelList(ListView):
    template_name = 'core/vehicle/model_list.html'
    model = Modell


class VehicleList(ListView):
    template_name = 'core/vehicle/vehicle_list.html'
    model = Vehicle


class DealershipList(ListView):
    template_name = 'core/dealership/dealership_list.html'
    model = Dealership


class StoreList(ListView):
    template_name = 'core/store/store_list.html'
    model = Store

# @login_required
# def user_profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/accounts/loggedin')
#     else:
#         user = request.user
#         profile = user.profile
#         form = UserProfileForm(instance=profile)

#     args = {}
#     args.update(csrf(request))

#     args['form'] = form

#     return render_to_response('core/person/profile.html', args)
