rm db.sqlite3
rm -rf ./parkfitapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations parkfitapi
python3 manage.py migrate parkfitapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python manage.py loaddata trainers
python manage.py loaddata difficulties
python manage.py loaddata classes
python manage.py loaddata comments
python manage.py loaddata athletes
python manage.py loaddata athlete_classes


