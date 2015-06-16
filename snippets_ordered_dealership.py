from new_way.core.models import Ordered, Dealership
lista = []
ordereds = Ordered.objects.all()[:5]
for order in ordereds:
    for o in order.dealership.all():
        lista.append(o.dealership)

lista
len(lista)
