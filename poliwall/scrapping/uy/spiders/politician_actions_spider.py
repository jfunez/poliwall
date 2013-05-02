# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from uy.items import Action
from apps.polidata.models import Politician

base_url = "http://www.parlamento.gub.uy/forms2/fojaleg.asp?Legislaturas=47&Legislador=%s&LegislaturaCompleta=s"


START_URLS = []
for politician in Politician.objects.all():
    try:
        politician.actions.all().exists()
    except AttributeError:
        START_URLS.append(base_url % politician.politician_id)


class ActionSpider(BaseSpider):
    name = "actions"
    allowed_domains = ["parlamento.gub.uy", ]
    start_urls = START_URLS

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        actions = hxs.select('/html/body/div/center/table[position()>2]/tr')

        items = []
        n = 0
        for action in actions:
            n += 1
            tds = action.select('td')
            item = Action()
            if n == 1:   # Convocatoria
                try:
                    # en negrita
                    item['date'] = tds[0].select('.//strong/text()').extract()[0]
                    item['text'] = tds[2].select('.//div/strong/text()').extract()[0]
                except:
                    # normal
                    item['date'] = tds[0].select('.//text()').extract()[0]
                    item['text'] = tds[2].select('.//div/text()').extract()[0]
            else:
                item['date'] = tds[0].select('.//text()')[0].extract()
                # http://stackoverflow.com/questions/8066461/using-xpath-to-get-text-of-paragraph-with-links-inside
                # string() extracts all the text
                item['text'] = tds[2].select('string(.//div)').extract()[0]

            item['source_url'] = response.url
            item['politician_id'] = response.url.split('&')[1].split('=')[1]
            items.append(item)

        return items
