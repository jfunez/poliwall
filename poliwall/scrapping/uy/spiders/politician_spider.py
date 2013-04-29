# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from uy.items import Senator, Deputy, Politician
from extra_profile_urls import extra_urls

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
        name, description, party = vicepresident.extract().split('<br>')[1:4]
        last_name, first_name = name.split('<a href="#')[0].strip().split(',')
        item['first_name'] = first_name
        item['last_name'] = last_name
        item['party'] = party.strip()
        item['email'] = vicepresident.select('a/@href').extract()[1].split(':')[1].strip()
        item['photo_url'] = 'http://www.parlamento.gub.uy' + vicepresident.select('img/@src').extract()[0].strip()
        politician_id = item['photo_url'].split('Fot')[1].split('.')[0]
        item['profile_url'] = 'http://www.parlamento.gub.uy/palacio3/legisladores/legislador.asp?ID=%s%s' % (
            LEGISLATIVE, politician_id)
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
            item['profile_url'] = 'http://www.parlamento.gub.uy/palacio3/legisladores/legislador.asp?ID=%s%s' % (
                LEGISLATIVE, politician_id)
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
            item['profile_url'] = 'http://www.parlamento.gub.uy/palacio3/legisladores/legislador.asp?ID=%s%s' % (
                LEGISLATIVE, politician_id)
            items.append(item)
        return items


class PoliticianSpider(BaseSpider):
    name = "politician"
    allowed_domains = ["parlamento.gub.uy"]
    start_urls = ['http://www.parlamento.gub.uy/palacio3/legisladores/legislador.asp?id=%s' % x for x in extra_urls.keys()]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        fullid = response.url[-7:]
        fullname = extra_urls[fullid]
        last_name, first_name = fullname.strip().split(',')
        item = Politician()
        item['first_name'] = first_name.strip()
        item['last_name'] = last_name.strip()
        item['politician_id'] = response.url[-5:]
        item['profile_id'] = fullid
        if item['politician_id'] == '00479':
            item['role'] = u'Senador de la República'
            item['party'] = u'Partido Frente Amplio'
            item['state'] = u'MONTEVIDEO'
            item['legislative_id'] = u'XLVII'
        else:
            datos = [x.strip() for x in hxs.select('//*[@id="TblIdLeg"]//tr[2]//font//text()').extract()]
            role = ""
            party = ""
            state = ""
            on_party = False
            on_state = False
            on_role = True
            if 'PRESIDENTE' in datos[0]:
                datos = datos[1:]
            for data in datos[0].split():
                if data == "PARTIDO":
                    on_party = True
                    on_role = False
                if data == "departamento":
                    on_party = False
                    on_state = True
                    continue
                if on_role:
                    role += data + ' '
                    continue
                if on_party:
                    party += data + ' '
                    continue
                if on_state:
                    if data != 'de':
                        state = data
            item['role'] = role.replace('por el Lema', '').replace('electo', '').strip()
            item['party'] = party.replace(', ', '')
            item['state'] = state.strip()
            item['legislative_id'] = datos[1].split(':')[1].replace('a.)', '').strip()
        try:
            item['email'] = datos[3].strip()
        except:
            pass
        item['photo_url'] = 'http://www.parlamento.gub.uy%s' % hxs.select('//img/@src')[0].extract()
        item['profile_url'] = response.url

        return item


class PoliticianBiographySpider(BaseSpider):
    name = "politicianbiography"
    allowed_domains = ["parlamento.gub.uy"]
    start_urls = ['http://www.parlamento.gub.uy/palacio3/legisladores/biografia.asp?id=%s' % x for x in extra_urls.keys()]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        fullid = response.url[-7:]
        fullname = extra_urls[fullid]
        last_name, first_name = fullname.strip().split(',')
        item = Politician()
        data = hxs.select('//*[@id="Table5"]//p').extract()
        item['biography'] = '\n'.join([u'%s' % p.strip() for p in data if p.strip()])
        item['profile_id'] = fullid
        return item
