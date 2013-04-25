# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from polidata.models import Legislative, Politician
from polisessions.models import House, Session


class Asistance(models.Model):

    """ Modelo para guardar las asistencias """

    legislative = models.Foreigkey(Legislative, verbose_name=_(u'Legislatura'), related_name='asistance_legislatives')
    politician = models.Foreigkey(Politician, verbose_name=_(u'Político'), related_name='asistance_politcians')
    house = models.Foreigkey(House, verbose_name=_(u'Cámara'), related_name='asistance_houses')
    session = models.Foreigkey(Session, verbose_name=_(u'Sesión'), related_name='asistance_sessions')
    was_there = models.BooleanField(_(u'Asistió?'), default=True, db_index=True)
    has_ad_to_absence = models.BooleanField(_(u'Con aviso de falta?'), default=False, db_index=True)
    has_license = models.BooleanField(_(u'Con licencia?'), default=False, db_index=True)
    was_to_go_as_president = models.BooleanField(_(
        u'Cambio su rol a Presidente de la República?'), default=False, db_index=True)

    class Meta:
        verbose_name = _(u'Asistencia')
        verbose_name_plural = _(u'Asistencias')
