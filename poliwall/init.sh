#!/bin/bash
DB_NAME="poliwall"
SUPERUSER_NAME="admin"
SUPERUSER_MAIL="admin@poliwall.com"
pip install -r requirements.txt
export PYTHONPATH=`pwd`:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=poliwall.settings
dropdb $DB_NAME
createdb -E UTF8 $DB_NAME
python manage.py syncdb --migrate --noinput
python manage.py loaddata scrapping/initial_legislative.json
python manage.py createsuperuser --username=$SUPERUSER_NAME --email=$SUPERUSER_MAIL
cd scrapping
scrapy crawl politician --nolog
scrapy crawl politicianbiography --nolog
cd ..
./viaticos.sh
