from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from pro_tips.apps.tips import models
from pro_tips.apps.api import serializers

class ListLanguages(generics.ListCreateAPIView):
    queryset = models.Languages.objects.all()
    serializer_class = serializers.LanguageSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    paginate_by = 100


class ListTips(generics.ListCreateAPIView):
    queryset = models.Tip.objects.all()
    serializer_class = serializers.TipSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    paginate_by = 100