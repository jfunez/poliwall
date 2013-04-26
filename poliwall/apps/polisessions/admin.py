# -*- coding: utf-8 -*-
from django.contrib import admin
from polisessions.models import Session, Action


class SessionAdmin(admin.ModelAdmin):
    pass


class ActionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Session, SessionAdmin)
admin.site.register(Action, ActionAdmin)
