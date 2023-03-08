# Mom_Infant

# Set up

`python manage.py migrate`

`python manage.py collectstatic`

`gunicorn garmin_server.wsgi:application -b:50000  --daemon`

# Lets encript ssl 
`sudo certbot --nginx -d pekko.d.umn.edu`