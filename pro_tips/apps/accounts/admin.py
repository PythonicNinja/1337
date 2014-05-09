# -*- coding: utf-8 -*-
from django.contrib import admin

from urban.apps.user_profiles.models import CUser


class CUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CUser, CUserAdmin)
