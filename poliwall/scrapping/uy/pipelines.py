# -*- coding: utf-8 -*-
from datetime import datetime
import urllib2
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from apps.polidata.models import Legislative, Politician, LegislativePolitician, Party, House


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


class DjangoStoragePipeline(object):

    def process_item(self, item, spider):
        if not spider.name in ['senators', 'deputies']:
            return item

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
            leg_pol.state = item['state'].title()

        leg_pol.save()
        return item


def to_date(date):
    if not date:
        return None
    return datetime.strptime(date, '%d/%m/%y').date()


def to_float(amount):
    if not amount:
        return None
    return float(amount.replace('.', '').replace(',', '.'))


class DiemDjangoStoragePipeline(object):

    def process_item(self, item, spider):
        if spider.name != 'diem':
            return item

        from apps.polidiem.models import Diem
        obj = Diem()

        obj.legislative = Legislative.objects.latest('end_date')

        first_name = item['first_name'].title()
        last_name = item['last_name'].title()

        try:
            obj.politician = Politician.objects.get(first_name=first_name, last_name=last_name)
        except Politician.DoesNotExist:
            politician = Politician(first_name=first_name, last_name=last_name)
            politician.save()
            obj.politician = politician

        obj.party = Party.objects.get(code=item['party'].upper())

        try:
            leg_pol = LegislativePolitician.objects.get(legislative=obj.legislative, politician=obj.politician,
                                                        party=obj.party)
            obj.house = leg_pol.house
        except LegislativePolitician.DoesNotExist:
            leg_pol = LegislativePolitician(date=datetime.now(), legislative=obj.legislative, politician=obj.politician,
                                            party=obj.party)
            try:
                house = House.objects.get(rol_name__icontains=item['type'])
            except House.DoesNotExist:
                house = House(name=item['type'], role_name=item['type'])
                house.save()
            leg_pol.house = house
            leg_pol.save()
            obj.house = leg_pol.house

        obj.date = to_date(item['date'])
        obj.extra = item['extra']
        obj.number = item['number']
        obj.ol = item['ol']
        obj.place = item['place']
        obj.event = item['event']
        obj.days = int(item['days'])
        obj.start_date = to_date(item['start_date'])
        obj.end_date = to_date(item['end_date'])
        obj.ticket_cost = to_float(item['ticket_cost'])
        obj.travel_insurance = to_float(item['travel_insurance'])
        obj.diem = to_float(item['diem'])
        obj.report_refund = to_float(item['report_refund'])
        obj.report_date = to_date(item['report_date'])
        obj.report_rest = to_float(item['report_rest'])
        obj.total_trip = to_float(item['total_trip'])
        obj.observations = item['observations']

        obj.save()

        return item



