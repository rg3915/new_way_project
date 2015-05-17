from new_way.core.models import Ordered
from django.db.models import Count


class VehicleAgeMixin(object):

    def get_context_data(self, **kwargs):
        ''' Veiculos mais consultados por faixa de idade '''
        context = super(VehicleAgeMixin, self).get_context_data(**kwargs)
        v = Ordered.objects.values('vehicle__vehicle').annotate(
            consultados=Count('vehicle')).order_by('-consultados')
        context['vehicles_age'] = v
        return context
