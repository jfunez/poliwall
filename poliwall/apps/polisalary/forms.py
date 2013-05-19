# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from polisalary.models import PoliticianSalary
from polidata.models import House, Legislative, LegislativePolitician, Politician


def get_houses():
    return House.objects.all().values_list('pk', 'name')


class SetSalaryForm(forms.Form):
    date = forms.DateField(label=_(u'Fecha'))
    house = forms.ChoiceField(label=_(u'Cámara'), choices=get_houses())
    amount = forms.FloatField(label=_(u'Monto'))

    def save(self, *args, **kwargs):
        # {'date': datetime.date(2012, 6, 1), 'house': u'1', 'amount': 1.0}
        data = self.cleaned_data
        legislatures = Legislative.objects.exclude(start_date__gt=data['date']).filter(end_date__gte=data['date']).values_list('pk', flat=True)
        qs = LegislativePolitician.objects.filter(legislative__in=legislatures, house=data['house'])
        politician_ids = qs.values_list('politician', flat=True)
        end_count = PoliticianSalary.objects.filter(end_date=None, politician__in=politician_ids).update(end_date=data['date'])
        new_salaries = []
        for pid in politician_ids:
            for leg in legislatures:
                new_salaries.append(PoliticianSalary(legislative_id=leg, amount=data['amount'], start_date=data['date'], politician_id=pid))
        new_count = PoliticianSalary.objects.bulk_create(new_salaries)

        return {
            'politician_updated': Politician.objects.filter(pk__in=politician_ids).iterator(),
        }
