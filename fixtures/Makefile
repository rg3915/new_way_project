brand:
	python csv2json.py fixtures/marcas.csv core.Brand

load_brand:
	python ../manage.py loaddata fixtures/marcas.csv.json

modell:
	python csv2json.py fixtures/modelos.csv core.Modell

load_modell:
	python ../manage.py loaddata fixtures/modelos.csv.json

kit:
	python csv2json.py fixtures/kit.csv core.Kit

load_kit:
	python ../manage.py loaddata fixtures/kit.csv.json

vehicle:
	python csv2json.py fixtures/veiculos.csv core.Vehicle

load_vehicle:
	python ../manage.py loaddata fixtures/veiculos.csv.json

address:
	python csv2json.py fixtures/enderecos.csv core.Address

load_address:
	python ../manage.py loaddata fixtures/enderecos.csv.json

dealership:
	python csv2json.py fixtures/concessionarias.csv core.Dealership

load_dealership:
	python ../manage.py loaddata fixtures/concessionarias.csv.json

clear_json:
	rm fixtures/*.json

load_fixtures: brand load_brand modell load_modell kit load_kit vehicle load_vehicle address load_address dealership load_dealership clear_json