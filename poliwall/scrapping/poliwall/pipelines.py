from datetime import datetime
from apps.polidata.models import Legislative, Politician, LegislativePolitician, Party

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


class DjangoStoragePipeline(object):
    def process_item(self, item, spider):
        legislative = Legislative.objects.latest('end_date')

        try:
            politician = Politician.objects.get(first_name=item['first_name'], last_name=item['last_name'])
        except Politician.DoesNotExist:
            politician = Politician(**item)
            politician.save()

        party = Party.objects.get_or_create(name=item['party'])

        leg_pol = LegislativePolitician(date=datetime.now(), legislative=legislative, politician=politician,
                                        party=party)

        if spider == 'senators':
            leg_pol.role = 'S'
        elif spider == 'deputies':
            leg_pol.role = 'D'

        leg_pol.save()
        return item
