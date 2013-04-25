# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from uy.items import Diem


LEGISLATIVE = '47'


class DiemSpider(BaseSpider):
    name = "diem"
    start_urls = ["http://share.pdfonline.com/540ff470d9bd402088f252a2e86e3321/viaticos.htm", ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        lines = hxs.select('//td//p').extract()
        start = False
        itemsdata = []
        diemdata = []

        def parse_line(line):
            if not '>' in line:
                return line
            line = line.replace('<nobr>', '')
            line = line.replace('</nobr>', '')
            line = ''.join(''.join(line.split('>')[1:]).split('</')[:-1])
            if line == u'\xa0':
                line = ''
            return line
        for index, line in enumerate(lines):
            line = parse_line(line)
            if start:
                if 'Senador' in line and 'funcionario' in line:
                    start = False
                    continue
                if 'Totales' in line:
                    break
                if 'Nota del Sec' in line:
                    diemdata.append(line)
                    diemdata.append(line)
                diemdata.append(line)
                if len(diemdata) == 22:
                    itemsdata.append(tuple(diemdata))
                    diemdata = []
            elif line.lower() == 'observaciones':
                start = True

        items = []
        for index, itm in enumerate(itemsdata):
            item = Diem()
            item['first_name'] = itm[0].split(',')[1].strip()
            item['last_name'] = itm[0].split(',')[0].strip()
            item['type'] = itm[1]
            item['party'] = itm[2]
            item['date'] = itm[3]
            item['extra'] = itm[4]
            item['number'] = itm[5]
            item['ol'] = itm[6]
            item['place'] = itm[7]
            item['event'] = itm[8]
            item['days'] = itm[9]
            item['start_date'] = itm[10]
            item['end_date'] = itm[12]
            item['ticket_cost'] = itm[13]
            item['travel_insurance'] = itm[14]
            item['diem'] = itm[15]
            item['refund'] = itm[16]
            item['report_date'] = itm[17]
            item['report'] = itm[19]
            item['total_trip'] = itm[20]
            item['observations'] = itm[21]
            items.append(item)

        print items

curl --form "Filedata=@/home/jp/dev/repo/poliwall/ignore/viaticos.pdf" --form press=Upload --keepalive-time 40 http://www.pdfonline.com/convert-pdf-to-html/Default.aspx?op=upload&email= > salida.txt
http://www.pdfonline.com/convert-pdf-to-html/DocStorage/c941bd6b68b447c786e88257a2b4a6e2/viaticos.htm
