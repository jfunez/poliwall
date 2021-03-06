#!/bin/bash
export PYTHONPATH=`pwd`:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=poliwall.settings
export PDF_NAME='viaticos'
export PDF_URL="http://www.parlamento.gub.uy/VerDocEspecial.asp?DocumentoId=114"
PDF_SERVICE='http://www.pdfonline.com/convert-pdf-to-html/Default.aspx?op=upload&email='
PDF_URL_RESULT_HTML="http://www.pdfonline.com/convert-pdf-to-html/DocStorage/737c5a8b70a04e0eb8f69083a52ded3e/viaticos.htm"
curl -o $PDF_NAME.pdf $PDF_URL
PDF_PATH="`pwd`/$PDF_NAME.pdf"
curl -o $PDF_NAME.tmp -# --form "Filedata=@$PDF_PATH" --form press=Upload --keepalive-time 40 $PDF_SERVICE
PDF_URL_RESULT="http://www.pdfonline.com/convert-pdf-to-html/`cat $PDF_NAME.tmp | sed -e 's/<body>\(.*\)<\/body>/\1/' | sed -e 's/<html>\(.*\)<\/html>/\1/'`"
PDF_URL_RESULT_HTML="http://www.pdfonline.com/convert-pdf-to-html/`cat $PDF_NAME.tmp | sed -e 's/<body>\(.*\)<\/body>/\1/' | sed -e 's/<html>\(.*\)<\/html>/\1/' | cut -d"=" -f2 | sed -e 's/.zip&id/.htm/'`"
curl -o $PDF_NAME.tmp2 $PDF_URL_RESULT
rm $PDF_NAME.tmp*
rm $PDF_NAME.pdf*
python manage.py syncdb --migrate --noinput
python manage.py loaddata scrapping/initial_houses.json
cd scrapping
echo $PDF_URL_RESULT_HTML
scrapy crawl diem -a start_url="$PDF_URL_RESULT_HTML" --nolog
