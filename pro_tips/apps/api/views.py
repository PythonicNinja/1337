from django.contrib.comments import Comment
from django.contrib.comments.templatetags.comments import CommentListNode
from django.contrib.sites.models import Site
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics
from rest_framework import views
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from pro_tips.apps.tips.models import Tip, Languages
from pro_tips.apps.api import serializers

class LanguagesView(generics.ListCreateAPIView):
    queryset = Languages.objects.all()
    serializer_class = serializers.LanguageSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    paginate_by = 100


class TipsView(generics.ListCreateAPIView):
    queryset = Tip.objects.all()
    serializer_class = serializers.TipSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user', 'title', 'language')
    paginate_by = 100


class LanguagesList(generics.ListAPIView):
    queryset = Languages.objects.all()
    serializer_class = serializers.LanguageSerializer
    paginate_by = 100


class TipsList(generics.ListAPIView):
    queryset = Tip.objects.all()
    serializer_class = serializers.TipSerializer
    filter_fields = ('user', 'title', 'language')
    filter_backends = (filters.DjangoFilterBackend,)
    paginate_by = 4


class CommentsList(views.APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)


    def get(self, request, format=None):
        '''
            returns comment for tip
        '''
        tip = get_object_or_404(Tip, pk=request.GET.get('id'))
        site = Site.objects.get_current()
        comments = Comment.objects.for_model(tip).filter(site = site, is_public = True, is_removed = False)
        return Response(comments)


