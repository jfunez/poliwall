# -*- coding: utf-8 -*-
from django.contrib import admin

from polisessions.models import Session, Action


class SessionAdmin(admin.ModelAdmin):
    list_display = ('legislative', 'house', 'date', 'number', 'short_name', 'ordinal', 'president')


class ActionAdmin(admin.ModelAdmin):
    list_display = ('legislative', 'session', 'politician')


admin.site.register(Session, SessionAdmin)
admin.site.register(Action, ActionAdmin)
