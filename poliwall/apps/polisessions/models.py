# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from polidata.models import Legislative, House, Politician


class Session(models.Model):

    """ Modelo para guardar las sesiones """

    legislative = models.ForeignKey(Legislative, verbose_name=_(u'Legislatura'), related_name='legislatives')
    house = models.ForeignKey(House, verbose_name=_(u'Cámara'), related_name='houses')
    date = models.DateField(_(u'Fecha'))
    short_name = models.CharField(_(u'Nombre corto'), max_length=100)
    ordinal = models.IntegerField(_(u'Ordinal'))
    president = models.ForeignKey(Politician, verbose_name=_(u'Preside'), related_name='presidents')
    source_url = models.TextField(_(u'Link de la fuente'))
    assists_text = models.TextField(_(u'Texto Asistencias'))

    class Meta:
        verbose_name = _(u'Sesion')
        verbose_name_plural = _(u'Sesiones')

    def __unicode__(self):
        return u'%s' % self.name


class Action(models.Model):

    """ Modelo para actuaciones las sesiones por político """

    legislative = models.ForeignKey(Legislative, verbose_name=_(u'Legislatura'), related_name='legislatives')
    session = models.ForeignKey(Session, verbose_name=_(u'Sesión'))
    source_url = models.TextField(_(u'Link de la fuente'))
    politician = models.ForeignKey(Politician, verbose_name=_(u'Político'), related_name='politicians')
    text = models.TextField(_(u'Texto'))

    class Meta:
        verbose_name = _(u'Actuación')
        verbose_name_plural = _(u'Actuaciones')

    def __unicode__(self):
        return u'[%s] %s: "%s"' % (self.date.strftime('%d/%m/%Y'), self.politician, self.text)
