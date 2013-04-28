# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from polidata.models import Legislative, Politician, Party, House


class Diem(models.Model):

    """ Modelo para guardar los viajes y viaticos de los políticos """

    legislative = models.ForeignKey(Legislative, verbose_name=_(u'Legislatura'), related_name='diem_legislatives')
    politician = models.ForeignKey(Politician, verbose_name=_(u'Político'), related_name='diem_politcians')
    house = models.ForeignKey(House, verbose_name=_(u'Rol'), blank=True, null=True)
    party = models.ForeignKey(Party, verbose_name=_(u'Partido'), blank=True, null=True)
    # Resolution
    date = models.DateField(_(u'Fecha'), blank=True, null=True)
    extra = models.CharField(_(u'S/F'), max_length=100)
    number = models.CharField(_(u'Número'), max_length=100, blank=True, null=True)
    # OL
    ol = models.CharField(_(u'OL'), max_length=10)
    # Destiny
    place = models.CharField(_(u'Lugar'), max_length=200)
    event = models.CharField(_(u'Evento'), max_length=200)
    # Mision
    days = models.PositiveIntegerField(_(u'Días'))
    start_date = models.DateField(_(u'Inicio'))
    end_date = models.DateField(_(u'Fin'))
    # U$S
    ticket_cost = models.FloatField(_(u'Pasaje'), blank=True, null=True)
    travel_insurance = models.FloatField(_(u'Seguro de Viaje'), blank=True, null=True)
    diem = models.FloatField(_(u'Viático'), blank=True, null=True)
    # Report U$S
    report_refund = models.FloatField(_(u'Devuelve'), blank=True, null=True)
    report_date = models.DateField(_(u'Fecha'), blank=True, null=True)
    report_rest = models.FloatField(_(u'Gastos'), blank=True, null=True)
    # Total trip
    total_trip = models.FloatField(_(u'Total del viaje'))
    # Observations
    observations = models.TextField(_(u'Observaciones'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Viático')
        verbose_name_plural = _(u'Viáticos')

    def __unicode__(self):
        return u'%s - %s U$S %s' % (self.politician, self.event, self.total_trip)
