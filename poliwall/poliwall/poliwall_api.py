# -*- coding: utf-8 -*-
from tastypie.api import Api
from polidata.api import (
    PartyResource,
    SubPartyResource,
    LegislativeResource,
    PoliticianResource,
    LegislativePoliticianResource,
)

v1_api = Api(api_name='v1')
v1_api.register(PartyResource())
v1_api.register(SubPartyResource())
v1_api.register(LegislativeResource())
v1_api.register(PoliticianResource())
v1_api.register(LegislativePoliticianResource())
