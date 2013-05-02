# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest

from uy.items import Politician


class BasePoliticianSpider(BaseSpider):
    allowed_domains = ["parlamento.gub.uy"]
    start_urls = ['http://www.parlamento.gub.uy/palacio3/legisladores_der.asp', ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        urls = hxs.select('//table//tr//td//a//@href').extract()
        urls.insert(0, u'p_legisladores.asp?Legislatura=47')
        for url in urls:
            xurl = "http://www.parlamento.gub.uy/palacio3/%s" % url.replace('p_legisladores', 'legisladores_der')
            yield Request(xurl, callback=self.parse_legislative)

    def parse_legislative(self, response):
        yield FormRequest.from_response(response,
                                        formname='Form1',
                                        formdata={'Deptos': 'TODOS',
                                                  'ir.x': '14',
                                                  'ir.y': '11',
                                                  }, callback=self.parse_politicianprofile)

    def parse_politicianprofile(self, response):
        raise NotImplemented


class PoliticianProfileSpider(BasePoliticianSpider):
    name = "plinks"
    profiles = {}

    def parse_politicianprofile(self, response):
        hxs = HtmlXPathSelector(response)
        keys = hxs.select('//select[2]//option//@value').extract()[2:]
        values = hxs.select('//select[2]//option//text()').extract()[2:]
        newprofiles = dict([(unicode(k.split("=")[1]), v) for k, v in zip(keys, values)])
        self.profiles.update(newprofiles)
        for k, v in newprofiles.items():
            yield Request("http://www.parlamento.gub.uy/palacio3/legisladores/legislador.asp?id=%s" % k, callback=self.parse_profile_data)

    def parse_profile_data(self, response):
        hxs = HtmlXPathSelector(response)
        fullid = unicode(response.url[-7:])
        fullname = self.profiles[unicode(fullid)]
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


class PoliticianBiographySpider(BasePoliticianSpider):
    name = "politicianbiography"
    poli_ids = []

    def parse_politicianprofile(self, response):
        hxs = HtmlXPathSelector(response)
        keys = hxs.select('//select[2]//option//@value').extract()[2:]
        values = hxs.select('//select[2]//option//text()').extract()[2:]
        newprofiles = dict([(unicode(k.split("=")[1]), v) for k, v in zip(keys, values)])
        for k, v in newprofiles.items():
            politician_id = k[-7:]
            if politician_id in self.poli_ids:
                continue
            self.poli_ids.append(politician_id)
            yield Request("http://www.parlamento.gub.uy/palacio3/legisladores/biografia.asp?id=%s" % k, callback=self.parse_biography)

    def parse_biography(self, response):
        hxs = HtmlXPathSelector(response)
        fullid = unicode(response.url[-7:])
        item = Politician()
        fullid = response.url[-7:]
        item = Politician()
        data = hxs.select('//text()').extract()
        item['biography'] = '\n'.join([u'<p>%s</p>' % x for x in [p.strip() for p in data if p.strip()][2:]])
        if not item['biography']:
            return None
        item['profile_id'] = unicode(fullid[2:])
        return item
