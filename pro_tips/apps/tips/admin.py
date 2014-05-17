# -*- coding: utf-8 -*-
from adminsortable import admin as sortable
from django.contrib import admin
from pro_tips.apps.tips.models import Tip, Vote, Favourite


class TipAdmin(admin.ModelAdmin):
    ordering = ('language',)
    list_display = ['language', 'user', 'title', 'description', 'created', 'rating']

    class Meta:
        model = Tip

    def rating(self, instance):
        return Vote.objects.get_rating_by_tip(instance)

    rating.allow_tags = True
    rating.short_description = 'Visitor'


class VoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Vote


class FavouriteAdmin(admin.ModelAdmin):
    class Meta:
        model = Favourite


admin.site.register(Tip, TipAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Favourite, FavouriteAdmin)
