migrate:
	rm -rf new_way/core/migrations
	./manage.py makemigrations core
	./manage.py migrate

mer:
	./manage.py graph_models -e -g -l dot -o modelagem/new_way.png core

mer_full:
	./manage.py graph_models -a -g -o modelagem/new_way_full.png