from new_way.core.models import Ordered, Customer
from django.db.models import Count


class VehicleMixin(object):

    def get_context_data(self, **kwargs):
        ''' Veiculos mais consultados por faixa de idade '''
        context = super(VehicleMixin, self).get_context_data(**kwargs)
        # v = Ordered.objects.values('vehicle__vehicle').annotate(
        # consultados=Count('vehicle')).order_by('-consultados')

        ''' veículos mais consultados por sexo '''
        genderF = Ordered.objects.values('vehicle') \
            .filter(customer__gender='F') \
            .annotate(quant=Count('vehicle')) \
            .order_by('-quant') \
            .values('vehicle__vehicle', 'quant')[:5]
        genderM = Ordered.objects.values('vehicle') \
            .filter(customer__gender='M') \
            .annotate(quant=Count('vehicle')) \
            .order_by('-quant') \
            .values('vehicle__vehicle', 'quant')[:5]

        ''' veículos mais consultados por bairro '''
        d = Ordered.objects.values('dealership__district') \
            .annotate(quant=Count('vehicle')) \
            .order_by('-quant') \
            .values('dealership__district', 'quant')[:5]

        ''' concessionárias que mais venderam '''
        c = Ordered.objects.values('dealership__dealership') \
            .annotate(quant=Count('vehicle')) \
            .order_by('-quant') \
            .values('dealership__dealership', 'quant')[:5]

        ''' veículos mais vendidos '''
        q = Ordered.objects.values('vehicle__vehicle') \
            .annotate(quant=Count('vehicle')) \
            .order_by('-quant') \
            .values('vehicle__vehicle', 'quant')[:7]

        ''' último pedido '''
        l = Ordered.objects.all()[:5]

        # context['vehicles_age'] = v
        context['genderF'] = genderF
        context['genderM'] = genderM
        context['vehicleD'] = d
        context['vehicleC'] = c
        context['saleds'] = q
        context['last_ordereds'] = l
        return context


class CountMixin(object):

    def get_context_data(self, **kwargs):
        context = super(CountMixin, self).get_context_data(**kwargs)
        ''' veículo mais consultados por bairro '''
        d = Ordered.objects.values('dealership__district') \
            .annotate(quant=Count('vehicle')) \
            .order_by('-quant') \
            .values('dealership__district', 'quant')[:1]

        ''' concessionária que mais vendeu '''
        c = Ordered.objects.values('dealership__dealership') \
            .annotate(quant=Count('vehicle')) \
            .order_by('-quant') \
            .values('dealership__dealership', 'quant')[:1]

        ''' veículo mais vendido '''
        q = Ordered.objects.values('vehicle__vehicle') \
            .annotate(quant=Count('vehicle')) \
            .order_by('-quant') \
            .values('vehicle__vehicle', 'quant')[:1]

        ''' último pedido '''
        l = Ordered.objects.order_by('id').last()

        if d:
            context['vd'] = d[0]
        context['vc'] = c
        context['vq'] = q
        context['last_order'] = l
        return context
