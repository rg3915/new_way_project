from new_way.core.models import Ordered, Customer
from django.db.models import Count


class VehicleAgeMixin(object):

    def get_context_data(self, **kwargs):
        ''' Veiculos mais consultados por faixa de idade '''
        context = super(VehicleAgeMixin, self).get_context_data(**kwargs)
        v = Ordered.objects.values('vehicle__vehicle').annotate(
            consultados=Count('vehicle')).order_by('-consultados')

        ''' veículos mais consultados por sexo '''
        genders = Customer.objects.values('gender').annotate(
            quant=Count('gender')).order_by('gender')
        total_items = Customer.objects.count()
        genders = [
            {'gender': g['gender'], 'value': int(g['quant'] * 100 / total_items)} for g in genders]

        context['vehicles_age'] = v
        context['genders'] = genders
        return context
