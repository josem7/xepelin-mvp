docker-compose run api poetry run black . \
    && docker-compose run api poetry run prospector \
    && docker-compose run api python3 manage.py test -v 2
