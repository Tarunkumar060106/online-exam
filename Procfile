web: gunicorn onlinequiz.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn onlinequiz.wsgi