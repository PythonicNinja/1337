# -*- coding: utf-8 -*-
from django.contrib import admin

from models import CUser


class CUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CUser, CUserAdmin)
