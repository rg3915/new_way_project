heroku pg:reset DATABASE
heroku run python manage.py syncdb
heroku run python manage.py loaddata fixtures.json
