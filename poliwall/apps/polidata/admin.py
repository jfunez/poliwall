# -*- coding: utf-8 -*-
from django.contrib import admin
from polidata.models import Party, SubParty, Legislative, Politician, LegislativePolitician


class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', )


class SubPartyAdmin(admin.ModelAdmin):
    list_display = ('party', 'name')
    list_filter = ('party',)


class LegislativeAdmin(admin.ModelAdmin):
    list_display = ('code', 'start_date', 'end_date')


class PoliticianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'photo', 'profile_url')


class LegislativePoliticianAdmin(admin.ModelAdmin):
    list_display = ('date', 'legislative', 'politician', 'role', 'party', 'subparty')
    list_filter = ('legislative', 'party', 'subparty', 'role')


admin.site.register(Party, PartyAdmin)
admin.site.register(SubParty, SubPartyAdmin)
admin.site.register(Legislative, LegislativeAdmin)
admin.site.register(Politician, PoliticianAdmin)
admin.site.register(LegislativePolitician, LegislativePoliticianAdmin)
