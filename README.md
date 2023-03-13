# Mom_Infant

# Set up

`python manage.py migrate`

`python manage.py collectstatic`

`gunicorn Mom_Infant.wsgi:application -b:59000 --worker-class gevent --daemon`

# Lets encript ssl 
`sudo certbot --nginx -d pekko.d.umn.edu`