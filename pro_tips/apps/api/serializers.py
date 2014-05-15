# -*- coding: utf-8 -*-
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

