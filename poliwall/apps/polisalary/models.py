# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from polidata.models import Politician


class PoliticianSalary(models.Model):

    """ Modelo para guardar los sueldos de los políticos """

    politician = models.ForeignKey(Politician, verbose_name=_(
        u'Político'), related_name='salaries')
    start_date = models.DateField(_(u'Desde'))
    end_date = models.DateField(_(u'Hasta'), blank=True, null=True)
    amount = models.FloatField(_(u'Monto'))

    class Meta:
        verbose_name = _(u'Salario')
        verbose_name_plural = _(u'Salarios')
