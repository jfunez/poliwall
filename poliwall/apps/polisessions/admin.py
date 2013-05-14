# -*- coding: utf-8 -*-
from django.contrib import admin

from polisessions.models import Session, Action, ActionCategory


class SessionAdmin(admin.ModelAdmin):
    list_display = ('legislative', 'house', 'date', 'number', 'short_name', 'ordinal', 'president')


class ActionAdmin(admin.ModelAdmin):
    list_display = ('legislative', 'session', 'politician', 'category')


class ActionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Session, SessionAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(ActionCategory, ActionCategoryAdmin)

