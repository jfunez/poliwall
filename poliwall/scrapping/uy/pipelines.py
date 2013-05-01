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


def to_date(date):
    if not date:
        return None
    # Fix for unformated data
    date = date.replace('/', '')
    date = date[:2] + '/' + date[2:4] + '/' + date[-2:]
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
        try:
            obj.legislative = Legislative.objects.latest('end_date')

            first_name = item['first_name'].title().strip()
            last_name = item['last_name'].title().strip()

            politicians = list(Politician.objects.filter(first_name__icontains=first_name, last_name__icontains=last_name))
            if politicians:
                if len(politicians) == 1:
                    obj.politician = politicians[0]
                else:
                    politicians_id = LegislativePolitician.objects.all().filter(politician__in=politicians, party__code=item['party']).distinct().values_list('politician', flat=True)
                    if len(politicians_id) == 1:
                        obj.politician = Politician.objects.get(pk=politicians_id[0])
                    else:
                        rlist = []
                        leg_polis = LegislativePolitician.objects.all().filter(politician__in=politicians)
                        for lp in leg_polis:
                            if item['party'] in ''.join([x[0] for x in lp.party.name.replace('-', ' ').split()[1:]]):
                                rlist.append(lp)
                        if len(rlist) == 1:
                            obj.politician = rlist[0].politician
                        else:
                            fix1 = Politician.objects.get(profile_id='02920')
                            if fix1 in politicians:
                                obj.politician = fix1
                            else:
                                fix2 = Politician.objects.get(profile_id='00623')
                                if fix2 in politicians:
                                    obj.politician = fix2
                                else:
                                    print "ERROR CON: %s" % politicians
                                    return item
            else:
                politician = Politician(first_name=first_name, last_name=last_name)
                politician.save()
                obj.politician = politician

            try:
                obj.party = Party.objects.get(code=item['party'].upper())
            except Party.DoesNotExist:
                obj.party, created = Party.objects.get_or_create(name=item['party'].upper(), code=item['party'].upper())

            try:
                leg_pol = LegislativePolitician.objects.get(legislative=obj.legislative, politician=obj.politician,
                                                            party=obj.party)
                obj.house = leg_pol.house
            except LegislativePolitician.DoesNotExist:
                leg_pol = LegislativePolitician(date=datetime.now(), legislative=obj.legislative, politician=obj.politician,
                                                party=obj.party)
                try:
                    house = House.objects.get(rol_name__istartswith=item['type'])
                except House.DoesNotExist:
                    house = House(name=item['type'], rol_name=item['type'])
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
            print u'Viático: %s' % obj.politician
        except Exception, e:
            print item
            print e

        return item


class PoliticianDjangoStoragePipeline(object):

    def process_item(self, item, spider):
        if not spider.name in ['politician', 'plinks']:
            return item
        try:
            legislative = Legislative.objects.get(roman_code=item['legislative_id'])

            first_name = item['first_name'].title().strip()
            last_name = item['last_name'].title().strip()
            try:
                politician = Politician.objects.get(
                    first_name__icontains=first_name, last_name__icontains=last_name, profile_id=item['profile_id'][2:])
            except Politician.DoesNotExist:
                politician = Politician(first_name=first_name, last_name=last_name, email=item.get('email', ''),
                                        profile_url=item['profile_url'], profile_id=item['profile_id'][2:])

                if item['photo_url']:
                    filename = item['photo_url'].split('/')[-1]

                    img_temp = NamedTemporaryFile(delete=True)
                    img_temp.write(urllib2.urlopen(item['photo_url']).read())
                    img_temp.flush()
                    politician.photo.save(filename, File(img_temp))

                politician.save()

            party_name = item['party'].title().strip()
            party_code = ''.join([list(word)[0] for word in party_name.split(' ') if word][1:])
            party, party_created = Party.objects.get_or_create(name=party_name, code=party_code)

            try:
                leg_pol = LegislativePolitician.objects.get(legislative=legislative, politician=politician, party=party)
            except LegislativePolitician.DoesNotExist:
                leg_pol = LegislativePolitician(date=legislative.start_date, legislative=legislative, politician=politician, party=party)

            try:
                house = House.objects.get(rol_name__icontains=item['role'].split()[0])
            except House.DoesNotExist:
                house = House(name=item['role'], rol_name=item['role'].split()[0])
                house.save()

            leg_pol.house = house
            leg_pol.state = item.get('state', '').title()
            leg_pol.save()
            print u'%s - Perfil #%s: %s' % (legislative.code, politician.pk, politician)
        except Exception, e:
            print item
            print e

        return item


class PoliticianBiographyDjangoStoragePipeline(object):

    def process_item(self, item, spider):
        if not spider.name in ['politicianbiography', ]:
            return item
        try:
            if item['biography']:
                politician = Politician.objects.get(profile_id=item['profile_id'])
                politician.biography = item['biography']
                politician.save()
                print u'Biography: %s' % politician
        except Exception, e:
            import pdb
            pdb.set_trace()
            print item
            print e

        return item
