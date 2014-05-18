# -*- coding: utf-8 -*-
from rest_framework.fields import Field

__author__ = 'wojtek'

from datetime import datetime
from django.db.models.fields import related

from rest_framework import serializers

from pro_tips.apps.tips import models


class LanguageSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField('get_img')

    class Meta:
        model = models.Languages

        # def get_img(self, obj):
        #     return obj.image.url


class TipSerializer(serializers.ModelSerializer):
    rating = Field(source="get_rating")
    favs = Field(source="get_favs")

    class Meta:
        model = models.Tip


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vote

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favourite