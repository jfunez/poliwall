# -*- coding: utf-8 -*-
from django.contrib import admin

from polidata.models import Party, SubParty, Legislative, Politician, LegislativePolitician, House


class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', )


class SubPartyAdmin(admin.ModelAdmin):
    list_display = ('party', 'name')
    list_filter = ('party',)


class LegislativeAdmin(admin.ModelAdmin):
    list_display = ('code', 'start_date', 'end_date')


class PoliticianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sex', 'email', 'photo_thumb', 'original_profile_url')
    list_filter = ('sex',)
    list_editable = ('sex',)

    def original_profile_url(self, instance):
        return u'<a href="%s" target="_blank">Profile original</a>' % (instance.profile_url)
    original_profile_url.allow_tags = True


class LegislativePoliticianAdmin(admin.ModelAdmin):
    list_display = ('date', 'legislative', 'politician', 'party', 'subparty', 'state', 'house')
    list_filter = ('legislative', 'party', 'subparty')


class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Party, PartyAdmin)
admin.site.register(SubParty, SubPartyAdmin)
admin.site.register(Legislative, LegislativeAdmin)
admin.site.register(Politician, PoliticianAdmin)
admin.site.register(LegislativePolitician, LegislativePoliticianAdmin)
admin.site.register(House, HouseAdmin)
