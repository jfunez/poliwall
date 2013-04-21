# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from polidata.models import Legislative, Politician


class Asistance(models.Model):

    """ Modelo para guardar las asistencias """

    legislative = models.Foreigkey(Legislative, verbose_name=_(u'Legislatura'))
    politician = models.Foreigkey(Politician, verbose_name=_(u'Político'))

    class Meta:
        verbose_name = _(u'Asistencia')
        verbose_name_plural = _(u'Asistencias')
