import json
from django.contrib.auth.decorators import login_required
from django.contrib.comments import Comment
from django.contrib.comments.templatetags.comments import CommentListNode
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.serializers import serialize
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from pro_tips.apps.accounts.models import CUser
from rest_framework import generics
from rest_framework import views
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from pro_tips.apps.tips.models import Tip, Languages, Vote, Favourite
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
    paginate_by = 8


class CommentsList(views.APIView):
    # authentication_classes = (SessionAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        '''
            returns comment for tip
        '''
        tip = get_object_or_404(Tip, pk=request.GET.get('id'))
        site = Site.objects.get_current()
        comments = Comment.objects.for_model(tip).filter(site=site, is_public=True, is_removed=False)
        res = []
        for comment in comments:
            res.append({
                'contents': comment.comment,
                'author': comment.user.username
            })
        return HttpResponse(json.dumps(res), content_type="application/json")


class VotesView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = serializers.VoteSerializer
    filter_fields = ('type', 'user', 'tip')
    filter_backends = (filters.DjangoFilterBackend,)
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    paginate_by = 100


class FavouriteView(generics.ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = serializers.FavouriteSerializer
    filter_fields = ('user', 'tip')
    filter_backends = (filters.DjangoFilterBackend,)
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    paginate_by = 100


def get_votes_for_tip(request, tip):
    tip = get_object_or_404(Tip, pk=tip)
    votes = Vote.objects.filter(tip=tip)
    positive = votes.filter(type=True).count()
    negative = votes.filter(type=False).count()
    res = {
        'positive': positive,
        'negative': negative
    }
    return HttpResponse(json.dumps(res), content_type="application/json")


def add_comment(request):
    payload = json.loads(request.body)

    tip_id = int(payload.get('tip_id'))
    tip = get_object_or_404(Tip, pk=tip_id)
    user = request.user
    comment_text = payload.get('comment_text')

    comment = Comment.objects.create(**{
        'user': user,
        'comment': comment_text,
        # tip = 13
        'content_type': ContentType.objects.get(pk=13),
        'site_id': Site.objects.first().pk,
        'object_pk': tip.pk
    })
    res = {
        'status': 'ok'
    }

    return HttpResponse(json.dumps(res), content_type="application/json")
