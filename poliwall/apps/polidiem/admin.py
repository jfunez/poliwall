# -*- coding: utf-8 -*-
from django.contrib import admin

from polidiem.models import Diem


class DiemAdmin(admin.ModelAdmin):
    list_display = ('legislative', 'politician', 'party', 'place', 'event', 'total_trip')
    list_filter = ('legislative', 'party', 'house')


admin.site.register(Diem, DiemAdmin)

