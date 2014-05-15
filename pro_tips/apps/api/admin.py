# -*- coding: utf-8 -*-
from django.contrib import admin
from pro_tips.apps.tips import models


class LanguageAdmin(admin.ModelAdmin):

    class Meta:
        model = models.Languages


admin.site.register(models.Languages, LanguageAdmin)
