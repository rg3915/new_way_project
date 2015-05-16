from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from .models import Customer, Dealership, Address, Brand, Modell, Vehicle, Store
from .forms import CustomerForm


def home(request):
    return render(request, 'index.html')


class CustomerCreate(CreateView):
    template_name = 'core/person/customer_create_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('home')  # 'customer_list'


class BrandList(ListView):
    template_name = 'core/vehicle/brand_list.html'
    model = Brand


class ModelList(ListView):
    template_name = 'core/vehicle/model_list.html'
    model = Modell
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ModelList, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        models = Modell.objects.all()
        var_get_search = self.request.GET.get('search_box')
        if var_get_search is not None:
            models = models.filter(modell__icontains=var_get_search)
        return models


class VehicleList(ListView):
    template_name = 'core/vehicle/vehicle_list.html'
    model = Vehicle


class DealershipList(ListView):
    template_name = 'core/dealership/dealership_list.html'
    model = Dealership

# todo search


class StoreList(ListView):
    template_name = 'core/store/store_list.html'
    model = Store
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(StoreList, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        stores = Store.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            stores = stores.filter(
                Q(store__icontains=q) | Q(city__icontains=q))
        return stores


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
