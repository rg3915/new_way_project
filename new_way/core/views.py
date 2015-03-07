from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from .models import Customer, Dealership, Address, Brand
from .forms import CustomerForm


def home(request):
    return render(request, 'index.html')


class CustomerForm(CreateView):
    template_name = 'core/person/customer_create_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('home')  # 'customer_list'


class CustomerList(ListView):
    template_name = 'core/person/customer_list.html'
    model = Customer


class BrandList(ListView):
    template_name = 'core/vehicle/brand_list.html'
    model = Brand


class DealershipList(ListView):
    template_name = 'core/dealership/dealership_list.html'
    model = Dealership

    def get_context_data(self, **kwargs):
        id_address = Address.objects.get(pk=self.kwargs['pk'])
        address = Dealership.objects.filter(address=id_address)
        context = super(DealershipList, self).get_context_data(**kwargs)
        context['address'] = address
        return context

'''
    def get_context_data(self, **kwargs):
        Objvenda = Sale.objects.get(pk=self.kwargs['pk'])
        ItensVenda = SaleDetail.objects.all().filter(sale=Objvenda)
        context = super(SaleDetailView, self).get_context_data(**kwargs)
        context['count'] = ItensVenda.count()
        context['Sale'] = Objvenda
        context['Itens'] = ItensVenda
        return context
'''


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
