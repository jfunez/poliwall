# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Party(models.Model):

    """ Modelo para guardar los partidos políticos """

    name = models.CharField(_('Nombre'), max_length=100)

    class Meta:
        verbose_name = u'Partido'
        verbose_name_plural = u'Partidos'

    def __unicode__(self):
        return u'%s' % self.name


class SubParty(models.Model):

    """ Modelo para guardar los lemas de un partido político """

    party = models.ForeignKey(Party)
    name = models.CharField(_('Nombre'), max_length=100)

    class Meta:
        verbose_name = u'Lema'
        verbose_name_plural = u'Lemas'

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.party)


class Legislative(models.Model):

    """ Modelo para guardar las legislaturas de gobierno """

    code = models.IntegerField(_('Código'))
    start_date = models.DateField(_('Fecha inicial'))
    end_date = models.DateField(_('Fecha final'))

    class Meta:
        verbose_name = u'Legislatura'
        verbose_name_plural = u'Legislaturas'

    def __unicode__(self):
        return u'%s (%s - %s)' % (self.code, self.start_date, self.end_date)


class Politician(models.Model):

    """ Modelo para guardar los datos personales de los políticos """

    first_name = models.CharField(_('Nombre'), max_length=100)
    last_name = models.CharField(_('Apellidos'), max_length=100)
    email = models.EmailField(_('Email'), blank=True, null=True)
    photo = models.ImageField(_('Foto'), upload_to='polidata/politician/photos/', blank=True, null=True)
    profile_url = models.TextField(_('Profile URL'), blank=True, null=True)

    class Meta:
        verbose_name = u'Político'
        verbose_name_plural = u'Políticos'

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

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


ROLE_CHOICES = (
    ('S', _('Senador')),
    ('D', _('Diputado')),
)


class LegislativePolitician(models.Model):

    """ Modelo para guardar las representaciones de cada político en distintas legislaturas """

    date = models.DateField(u'Fecha')
    legislative = models.ForeignKey(Legislative, verbose_name=u'Legislatura', related_name='politicians')
    politician = models.ForeignKey(Politician, verbose_name=u'Político', related_name='legislatives')
    party = models.ForeignKey(Party, verbose_name=u'Partido', blank=True, null=True)
    subparty = models.ForeignKey(SubParty, verbose_name=u'Lema', blank=True, null=True)
    role = models.CharField(_(u'Rol'), choices=ROLE_CHOICES, max_length=20)

    class Meta:
        verbose_name = u'Representacion Política'
        verbose_name_plural = u'Representaciones Políticas'

    def __unicode__(self):
        return u'%s (%s)' % (self.legislative, self.politician)
