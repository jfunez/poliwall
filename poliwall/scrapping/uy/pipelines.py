from datetime import datetime
import urllib2
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from apps.polidata.models import Legislative, Politician, LegislativePolitician, Party

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


class DjangoStoragePipeline(object):
    def process_item(self, item, spider):
        legislative = Legislative.objects.latest('end_date')

        first_name = item['first_name'].title()
        last_name = item['last_name'].title()

        try:
            politician = Politician.objects.get(first_name=first_name, last_name=last_name)
        except Politician.DoesNotExist:
            politician = Politician(first_name=first_name, last_name=last_name, email=item.get('email', ''),
                                    profile_url=item['profile_url'])

            if item['photo_url']:
                filename = item['photo_url'].split('/')[-1]

                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urllib2.urlopen(item['photo_url']).read())
                img_temp.flush()
                politician.photo.save(filename, File(img_temp))

            politician.save()

        party, created = Party.objects.get_or_create(name=item['party'].title())

        try:
            leg_pol = LegislativePolitician.objects.get(legislative=legislative, politician=politician,
                                                        party=party)
        except LegislativePolitician.DoesNotExist:
            leg_pol = LegislativePolitician(date=datetime.now(), legislative=legislative, politician=politician,
                                            party=party)

        if spider.name == 'senators':
            leg_pol.role = 'S'
        elif spider.name == 'deputies':
            leg_pol.role = 'D'

        leg_pol.save()
        return item
