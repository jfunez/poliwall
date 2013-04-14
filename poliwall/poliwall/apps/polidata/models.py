# -*- coding: utf-8 -*-
from django.db import models


class Party(models.Model):
    """ Modelo para guardar los partidos políticos """

    name = models.CharField(u'Nombre', max_length=100)

    class Meta:
        verbose_name = u'Partido'
        verbose_name_plural = u'Partidos'


class SubParty(models.Model):
    """ Modelo para guardar los lemas de un partido político """

    party = models.ForeignKey(Party)
    name = models.CharField(u'Nombre', max_length=100)

    class Meta:
        verbose_name = u'Lema'
        verbose_name_plural = u'Lemas'


class Legislative(models.Model):
    """ Modelo para guardar las legislaturas de gobierno """

    code = models.IntegerField(u'Código')
    start_date = models.DateField(u'Fecha inicial')
    end_date = models.DateField(u'Fecha final')

    class Meta:
        verbose_name = u'Legislatura'
        verbose_name_plural = u'Legislaturas'


class Politician(models.Model):
    """ Modelo para guardar los datos personales de los políticos """

    first_name = models.CharField(u'Nombre', max_length=100)
    last_name = models.CharField(u'Apellidos', max_length=100)
    email = models.EmailField(u'Email', blank=True, null=True)
    photo = models.ImageField(u'Foto', upload_to='/polidata/politician/photos/', blank=True, null=True)
    profile_url = models.TextField(u'Profile URL', blank=True, null=True)

    class Meta:
        verbose_name = u'Político'
        verbose_name_plural = u'Políticos'

    def _get_lp_for(self, date):
        qs = LegislativePolitician.objects.all()
        qs = qs.filter(date=date)
        if not qs.exists():
            return None
        return qs[0]

    def get_party_for(self, date):
        lp = self._get_lp_for(date)
        return getattr(lp, 'party', None)

    def get_subparty_for(self, date):
        lp = self._get_lp_for(date)
        return getattr(lp, 'subparty', None)


class LegislativePolitician(models.Model):
    """ Modelo para guardar las representaciones de cada político en distintas legislaturas """

    date = models.DateField(u'Fecha')
    legislative = models.ForeignKey(Legislative, verbose_name=u'Legislatura')
    politician = models.ForeignKey(Politician, verbose_name=u'Político')
    party = models.ForeignKey(Party, verbose_name=u'Partdio', blank=True, null=True)
    subparty = models.ForeignKey(SubParty, verbose_name=u'Lema', blank=True, null=True)

    class Meta:
        verbose_name = u'Representacion Política'
        verbose_name_plural = u'Representaciones Políticas'
