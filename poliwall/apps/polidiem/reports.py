# -*- coding: utf-8 -*-
from decimal import Decimal
from django.utils.translation import ugettext_lazy as _

from model_report.report import reports, ReportAdmin
from model_report.utils import sum_column

from polidiem.models import Diem, Politician
from polidata.models import LegislativePolitician


def custom_sum_column(values):
    return sum_column([v for v in values if v])


def custom_usd_format(value, instance):
    if value:
        return 'U$S %.2f' % Decimal(value)
    return 'U$S 0.00'


def filter_party_legislative(report, queryset):
    lp = LegislativePolitician.objects.filter(
        legislative=report.get_legislative())
    pids = set(lp.values_list('party', flat=True))
    pids = set(Diem.objects.filter(
        party__pk__in=pids).values_list('party', flat=True))
    return queryset.filter(pk__in=pids)


class DiemReport(ReportAdmin):
    title = _(u'Reporte de viáticos')
    template_name = 'model_report/diem_report.html'
    model = Diem
    fields = [
        'politician__politician_id',
        'self.politician.get_fullname',
        'party__name',
        'place',
        'diem',
        'report_refund',
        'report_rest',
        'total_trip',
    ]
    list_filter = ('party__name', '#.politician.get_fullname',)
    list_group_by = ('politician__politician_id', 'party__name',)
    list_serie_fields = ('party__name', 'politician__politician_id',
                         'diem', 'report_refund', 'report_rest', 'total_trip',)
    type = 'chart'
    chart_types = ('pie', 'column')
    override_field_choices = {
        'party__name': filter_party_legislative,
    }
    override_field_labels = {
        'politician__politician_id': lambda i, j: _(u'Id de Político'),
        'self.politician.get_fullname': lambda i, j: _(u'Político'),
        'party__name': lambda i, j: _(u'Partido'),
    }
    group_totals = {
        'diem': custom_sum_column,
        'report_refund': custom_sum_column,
        'report_rest': custom_sum_column,
        'total_trip': custom_sum_column,
    }
    override_field_formats = {
        'diem': custom_usd_format,
        'report_refund': custom_usd_format,
        'report_rest': custom_usd_format,
        'total_trip': custom_usd_format,
    }
    report_total = {
        'diem': custom_sum_column,
        'report_refund': custom_sum_column,
        'report_rest': custom_sum_column,
        'total_trip': custom_sum_column,
    }

    def get_grouper_text(self, value, field, model_field):
        try:
            return Politician.objects.get(politician_id=value).get_fullname
        except:
            return value


reports.register('viaticos', DiemReport)
