# -*- coding: utf-8 -*-
from adminsortable import admin as sortable
from django.contrib import admin
from pro_tips.apps.tips.models import Tip, Vote


class TipAdmin(admin.ModelAdmin):
    ordering = ('language',)
    list_display = ['language', 'user', 'title', 'description', 'created', 'rating']

    class Meta:
        model = Tip

    def rating(self, instance):
        return Vote.objects.get_rating_by_tip(instance)

    rating.allow_tags = True
    rating.short_description = 'Visitor'


admin.site.register(Tip, TipAdmin)
