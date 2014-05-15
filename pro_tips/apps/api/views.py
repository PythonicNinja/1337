from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from pro_tips.apps.tips import models
from pro_tips.apps.api import serializers

class ListLanguages(generics.ListAPIView):
    queryset = models.Languages.objects.all()
    serializer_class = serializers.LanguageSerializer
    paginate_by = 100