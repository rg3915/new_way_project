from new_way.core.models import Ordered
    lista = []
    ordereds = Ordered.objects.all()[:5]
    for order in ordereds:
        for o in order.dealership.all():
            lista.append(o.dealership)

    lista
len(lista)

# ----------------------------
from new_way.core.models import Ordered
ordereds = Ordered.objects.all()[:5]
for order in ordereds:
    print([o.dealership__address for o in order.dealership.all()])
