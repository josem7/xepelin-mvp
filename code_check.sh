docker-compose run mvp poetry run black . \
    && docker-compose run mvp poetry run prospector \
    && docker-compose run mvp python3 manage.py test -v 2
