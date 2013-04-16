from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from poliwall.items import Senator, Deputy


LEGISLATIVE = '47'


class SenatorSpider(BaseSpider):
    name = "senators"
    allowed_domains = ["parlamento.gub.uy"]
    start_urls = [
        "http://www.parlamento.gub.uy/GxEmule/IntcpoGrafico.asp?Fecha=13042013&Cuerpo=S&Integracion=S&Desde=15021985&Hasta=13042013&Dummy=13042013&TipoLeg=Act&Orden=Legislador&Grafico=s&Integracion=S&Ejecutar+Consulta=Ejecutar+Consulta",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        senators = hxs.select('/html/body/center/div/table[2]/tr/td')
        items = []

        vicepresident = senators[0]
        item = Senator()
        item['photo_url'] = vicepresident.select('img/@src').extract()
        items.append(item)

        for senator in senators[1:]:
            item = Senator()
            name, party = senator.extract().split('<br>')[1:3]
            last_name, first_name = name.split('<a href="#')[0].strip().split(',')
            item['first_name'] = first_name
            item['last_name'] = last_name
            item['party'] = party.strip()
            item['email'] = senator.select('a/@href').extract()[1].split(':')[1].strip()
            item['photo_url'] = 'http://www.parlamento.gub.uy' + senator.select('img/@src').extract()[0].strip()
            politician_id = item['photo_url'].split('Fot')[1].split('.')[0]
            item['profile_url'] = 'http://www.parlamento.gub.uy/palacio3/legisladores/legislador.asp?ID=%s%s' % (LEGISLATIVE, politician_id)
            items.append(item)
        return items


class DeputySpider(BaseSpider):
    name = "deputies"
    allowed_domains = ["parlamento.gub.uy"]
    start_urls = [
        "http://www.parlamento.gub.uy/GxEmule/IntcpoGrafico.asp?Fecha=13042013&Cuerpo=D&Integracion=D&Desde=15021985&Hasta=13042013&Dummy=13042013&TipoLeg=Act&Orden=Legislador&Grafico=s&Integracion=S&Ejecutar+Consulta=Ejecutar+Consulta",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        deputies = hxs.select('/html/body/center/div/table[2]/tr/td')
        items = []
        for deputy in deputies:
            item = Deputy()
            name, party, state = deputy.extract().split('<br>')[1:4]
            last_name, first_name = name.split('<a href="#')[0].strip().split(',')
            item['first_name'] = first_name
            item['last_name'] = last_name
            item['party'] = party.strip()
            item['state'] = state.strip()
            try:
                item['email'] = deputy.select('a/@href').extract()[1].split(':')[1].strip()
            except:
                pass
            item['photo_url'] = 'http://www.parlamento.gub.uy' + deputy.select('img/@src').extract()[0].strip()
            politician_id = item['photo_url'].split('Fot')[1].split('.')[0]
            item['profile_url'] = 'http://www.parlamento.gub.uy/palacio3/legisladores/legislador.asp?ID=%s%s' % (LEGISLATIVE, politician_id)
            items.append(item)
        return items
