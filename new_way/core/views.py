from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from .models import Customer, Dealership, Address, Brand, Modell, Vehicle, Store, Ordered, Accessory
from .forms import CustomerForm
from new_way.core.managers import VehicleMixin, CountMixin


def home(request):
    return render(request, 'index.html')


class CustomerCreate(CreateView):
    template_name = 'core/person/customer_create_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('home')


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
        q = self.request.GET.get('search_box')
        if q is not None:
            models = models.filter(modell__istartswith=q)
        return models


class VehicleList(ListView):
    template_name = 'core/vehicle/vehicle_list.html'
    model = Vehicle
    paginate_by = 15

    def get_queryset(self):
        cars = Vehicle.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            cars = cars.filter(vehicle__icontains=q)
        return cars


class VehicleDetail(DetailView):
    template_name = 'core/vehicle/vehicle_detail.html'
    model = Vehicle

    def get_context_data(self, **kwargs):
        context = super(VehicleDetail, self).get_context_data(**kwargs)
        vehicle = Vehicle.objects.get(pk=self.kwargs['pk'])
        return context


class AccessoryList(ListView):
    template_name = 'core/vehicle/accessory_list.html'
    model = Accessory
    paginate_by = 12

    def get_queryset(self):
        accessorys = Accessory.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            accessorys = accessorys.filter(accessory__istartswith=q)
        return accessorys


class DealershipList(ListView):
    template_name = 'core/dealership/dealership_list.html'
    model = Dealership
    paginate_by = 10

    def get_queryset(self):
        dealerships = Dealership.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            dealerships = dealerships.filter(dealership__istartswith=q)
        return dealerships


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


class Dashboard(VehicleMixin, CountMixin, TemplateView):
    template_name = 'core/dashboard.html'


# @login_required
class OrderedCreate(CreateView):
    template_name = 'core/ordered/ordered_create_form.html'
    model = Ordered
    success_url = reverse_lazy('vehicle_list')  # 'ordered_list'


class OrderedList(ListView):
    template_name = 'core/ordered/ordered_list.html'
    model = Ordered
    paginate_by = 10


class OrderedDetail(DetailView):
    template_name = 'core/ordered/ordered_detail.html'
    model = Ordered

    def get_context_data(self, **kwargs):
        context = super(OrderedDetail, self).get_context_data(**kwargs)
        ordered = Ordered.objects.get(pk=self.kwargs['pk'])
        return context


class UnderConstruction(TemplateView):
    template_name = "core/under_construction.html"

'''
https://www.technovelty.org/web/skipping-pages-with-djangocorepaginator.html
'''
