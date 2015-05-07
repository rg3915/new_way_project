occupation:
	python csv2json.py fixtures/cargos_.csv core.Occupation

load_occupation:
	python ../manage.py loaddata fixtures/cargos_.csv.json

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

dealership:
	python csv2json.py fixtures/concessionarias_.csv core.Dealership

load_dealership:
	python ../manage.py loaddata fixtures/concessionarias_.csv.json

store:
	python csv2json.py fixtures/estabelecimentos.csv core.Store

load_store:
	python ../manage.py loaddata fixtures/estabelecimentos.csv.json

customer:
	python gen_customers_csv.py
	python csv2json.py fixtures/clientes.csv core.Customer

load_customer:
	python ../manage.py loaddata fixtures/clientes.csv.json

employee:
	python gen_employees_csv.py
	python csv2json.py fixtures/funcionarios.csv core.Employee

load_employee:
	python ../manage.py loaddata fixtures/funcionarios.csv.json

users:
	python gen_users_csv.py
	python csv2json.py fixtures/usuarios.csv auth.User

load_users:
	python ../manage.py loaddata fixtures/usuarios.csv.json

clear_json:
	rm fixtures/*.json

load_fixtures: dealership load_dealership occupation load_occupation users load_users employee load_employee