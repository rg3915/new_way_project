migrate:
	rm -rf new_way/core/migrations
	./manage.py makemigrations core
	./manage.py migrate

migrate_all:
	rm new_way/db.sqlite3
	rm -rf new_way/core/migrations
	./manage.py makemigrations core
	./manage.py migrate
	./manage.py createsuperuser --username='admin' --email=''

fixtures:
	./manage.py loaddata fixtures.json

backup:
	./manage.py dumpdata --format=json --indent=2 core > fixtures.json

mer:
	./manage.py graph_models -e -g -l dot -o modelagem/new_way.png core

mer_full:
	./manage.py graph_models -a -g -o modelagem/new_way_full.png