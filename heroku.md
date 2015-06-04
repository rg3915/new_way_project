# heroku

heroku login
heroku create new-way
echo "web: gunicorn new_way.wsgi" >> Procfile
git push heroku master --force
heroku ps:scale web=1
heroku labs:enable user-env-compile
heroku open


[1]: https://toolbelt.heroku.com/debian