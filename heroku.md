# heroku

heroku login
echo "python-3.4.0" > runtime.txt
heroku create new_way
echo "web: gunicorn new_way.wsgi" > Procfile
# editar wsgi.py
git push heroku master --force
heroku ps:scale web=1
heroku labs:enable user-env-compile
heroku pg
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py loaddata fixtures.json
heroku open



[1]: https://toolbelt.heroku.com/debian