# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Party(models.Model):

    """ Modelo para guardar los partidos políticos """

    name = models.CharField(_(u'Nombre'), max_length=100)

    class Meta:
        verbose_name = _(u'Partido')
        verbose_name_plural = _(u'Partidos')

    def __unicode__(self):
        return u'%s' % self.name


class SubParty(models.Model):

    """ Modelo para guardar los lemas de un partido político """

    party = models.ForeignKey(Party)
    name = models.CharField(_(u'Nombre'), max_length=100)

    class Meta:
        verbose_name = _(u'Lema')
        verbose_name_plural = _(u'Lemas')

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.party)


class Legislative(models.Model):

    """ Modelo para guardar las legislaturas de gobierno """

    code = models.IntegerField(_(u'Código'))
    start_date = models.DateField(_(u'Fecha inicial'))
    end_date = models.DateField(_(u'Fecha final'))

    class Meta:
        verbose_name = _(u'Legislatura')
        verbose_name_plural = _(u'Legislaturas')

    def __unicode__(self):
        return u'%s (%s - %s)' % (self.code, self.start_date, self.end_date)


SEX_CHOICES = (
    ('M', _(u'Masculino')),
    ('F', _(u'Femenino')),
)


class Politician(models.Model):

    """ Modelo para guardar los datos personales de los políticos """

    first_name = models.CharField(_(u'Nombre'), max_length=100)
    last_name = models.CharField(_(u'Apellidos'), max_length=100)
    email = models.EmailField(_(u'Email'), blank=True, null=True)
    photo = models.ImageField(_(u'Foto'), upload_to='polidata/politician/photos/', blank=True, null=True)
    sex = models.CharField(_(u'Genero'), max_length=1, choices=SEX_CHOICES, default='M')
    profile_url = models.TextField(_(u'Profile URL'), blank=True, null=True)
    twitter_user = models.CharField(_(u'Cuenta de Twitter'), max_length=100, blank=True)

    class Meta:
        verbose_name = _(u'Político')
        verbose_name_plural = _(u'Políticos')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def _get_lp_for(self, date=None):
        qs = LegislativePolitician.objects.filter(politician__pk=self.pk)
        if date:
            qs = qs.filter(date=date)
        else:
            qs = qs.order_by('-date')
        if not qs.exists():
            return None
        return qs[0]

    def get_party_for(self, date=None):
        lp = self._get_lp_for(date)
        return getattr(lp, 'party', None)

    def get_subparty_for(self, date=None):
        lp = self._get_lp_for(date)
        return getattr(lp, 'subparty', None)

    @property
    def get_current_party(self):
        return self.get_party_for(date=None)

    @property
    def get_current_subparty(self):
        return self.get_subparty_for(date=None)

    def photo_thumb(self):
        return '<img src="%s%s"/>' % (settings.MEDIA_URL, self.photo)
    photo_thumb.allow_tags = True


ROLE_CHOICES = (
    ('S', _(u'Senador')),
    ('D', _(u'Diputado')),
)


class LegislativePolitician(models.Model):

    """ Modelo para guardar las representaciones de cada político en distintas legislaturas """

    date = models.DateField(u'Fecha')
    legislative = models.ForeignKey(Legislative, verbose_name=u'Legislatura', related_name='politicians')
    politician = models.ForeignKey(Politician, verbose_name=u'Político', related_name='legislatives')
    party = models.ForeignKey(Party, verbose_name=u'Partido', blank=True, null=True)
    subparty = models.ForeignKey(SubParty, verbose_name=u'Lema', blank=True, null=True)
    state = models.CharField(_('Departamento'), max_length=100, blank=True, null=True)
    role = models.CharField(_(u'Rol'), choices=ROLE_CHOICES, max_length=20)

    class Meta:
        verbose_name = _(u'Representacion Política')
        verbose_name_plural = _(u'Representaciones Políticas')

    def __unicode__(self):
        return u'%s (%s)' % (self.legislative, self.politician)
