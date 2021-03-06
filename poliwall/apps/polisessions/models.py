# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from polidata.models import Legislative, House, Politician


class Session(models.Model):

    """ Modelo para guardar las sesiones """

    legislative = models.ForeignKey(Legislative, verbose_name=_(u'Legislatura'), related_name='session_legislatives')
    house = models.ForeignKey(House, verbose_name=_(u'Cámara'), related_name='session_houses')
    date = models.DateField(_(u'Fecha'))
    number = models.IntegerField(_(u'Número'), blank=True, null=True)
    short_name = models.CharField(_(u'Nombre corto'), max_length=100, blank=True, null=True)
    ordinal = models.IntegerField(_(u'Ordinal'), blank=True, null=True)
    president = models.ForeignKey(Politician, verbose_name=_(u'President'), related_name='presidents', blank=True, null=True)
    source_url = models.TextField(_(u'Link de la fuente'))
    assists_text = models.TextField(_(u'Texto Asistencias'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Sesion')
        verbose_name_plural = _(u'Sesiones')
        ordering = ['date', 'ordinal']

    def __unicode__(self):
        return u'Sesion %s Ordinal %s' % (self.date, self.ordinal)


class ActionCategory(models.Model):
    name = models.CharField(_(u'Nombre'), max_length=400)

    class Meta:
        verbose_name_plural = _(u'Action categories')

    def __unicode__(self):
        return self.name


class Action(models.Model):

    """ Modelo para actuaciones las sesiones por político """

    legislative = models.ForeignKey(Legislative, verbose_name=_(u'Legislatura'), related_name='legislative_actions')
    session = models.ForeignKey(Session, verbose_name=_(u'Sesión'))
    source_url = models.TextField(_(u'Link de la fuente'))
    politician = models.ForeignKey(Politician, verbose_name=_(u'Político'), related_name='actions')
    text = models.TextField(_(u'Texto'))
    category = models.ForeignKey(ActionCategory, blank=True, null=True)

    class Meta:
        verbose_name = _(u'Actuación')
        verbose_name_plural = _(u'Actuaciones')
        ordering = ['session']

    def __unicode__(self):
        return u'[%s - %s] Sesion %s' % (self.politician, self.pk, self.session)
