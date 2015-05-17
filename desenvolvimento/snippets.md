### Veiculos mais consultados por faixa de idade

faixa

18 -25	

25 -30	

30 -35	
	
**Resultado**

Veiculos	Consultados
Golf	80
Corsa	75
Palio	60
HB 20	50
Audi	45

*pode ser por modelo*

	from new_way.core.models import Ordered
	from django.db.models import Count
	v = Ordered.objects.values('vehicle__vehicle').annotate(consultados=Count('vehicle')).order_by('-consultados')
	[print(i) for i in v]