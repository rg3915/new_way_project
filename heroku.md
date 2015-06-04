# heroku

heroku login
echo "python-3.4.0" > runtime.txt
heroku create new_way
echo "web: gunicorn new_way.wsgi" > Procfile
git push heroku master --force
heroku ps:scale web=1
heroku pg
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku open

heroku labs:enable user-env-compile


[1]: https://toolbelt.heroku.com/debian