uwsgi --http :8080 --wsgi-file app.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191
