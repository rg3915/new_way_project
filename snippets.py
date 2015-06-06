from new_way.core.models import Ordered, Customer
from django.db.models import Count

''' veículos mais consultados por sexo '''
q = Ordered.objects.values('vehicle') \
    .filter(customer__gender='F') \
    .annotate(quant=Count('vehicle')) \
    .order_by('-quant') \
    .values('vehicle__vehicle', 'quant')
q
print(q.query)

print('\n')
''' veículos mais consultados por bairro '''
q = Ordered.objects.values('dealership__district') \
    .annotate(quant=Count('vehicle')) \
    .order_by('-quant') \
    .values('dealership__district', 'quant')
q
q.count()
print(q.query)

print('\n')
''' concessionárias que mais venderam '''
q = Ordered.objects.values('dealership__dealership') \
    .annotate(quant=Count('vehicle')) \
    .order_by('-quant') \
    .values('dealership__dealership', 'quant')
q
q.count()
print(q.query)

print('\n')
''' veículos mais vendidos '''
q = Ordered.objects.values('vehicle__vehicle') \
    .annotate(quant=Count('vehicle')) \
    .order_by('-quant') \
    .values('vehicle__vehicle', 'quant')
q
q.count()
print(q.query)

print('\n')
''' veículos mais consultados por faixa de idade '''

print('\n')
''' veículo mais consultado por bairro '''
q = Ordered.objects.values('dealership__district') \
    .annotate(quant=Count('vehicle')) \
    .order_by('-quant') \
    .values_list('dealership__district', 'quant')[:1]
q
for i in q:
    print(i.quant)
