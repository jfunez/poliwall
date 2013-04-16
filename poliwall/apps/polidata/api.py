# myapp/api.py
from tastypie.resources import ModelResource
from polidata.models import Party, SubParty, Legislative, Politician, LegislativePolitician


class GetOnly:
    allowed_methods = ['get']


class PartyResource(GetOnly, ModelResource):

    class Meta:
        queryset = Party.objects.all()


class SubPartyResource(GetOnly, ModelResource):

    class Meta:
        queryset = SubParty.objects.all()


class LegislativeResource(GetOnly, ModelResource):

    class Meta:
        queryset = Legislative.objects.all()


class PoliticianResource(GetOnly, ModelResource):

    class Meta:
        queryset = Politician.objects.all()


class LegislativePoliticianResource(GetOnly, ModelResource):

    class Meta:
        queryset = LegislativePolitician.objects.all()
