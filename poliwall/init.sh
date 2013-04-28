#!/bin/bash
pip install -r requirements.txt
export PYTHONPATH=`pwd`:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=poliwall.settings
dropdb poliwall
createdb -E UTF8 poliwall
python manage.py syncdb --migrate --noinput
python manage.py loaddata scrapping/initial_legislative.json
python manage.py createsuperuser --username=admin --email=admin@admin.com
cd scrapping
# scrapy crawl senators
# scrapy crawl deputies
scrapy crawl politician --nolog
cd ..
./viaticos.sh
