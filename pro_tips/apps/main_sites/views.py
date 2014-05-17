from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.template.response import TemplateResponse

from pro_tips.apps.tips.models import Tip, Languages

def index(request):
    ctx = {}
    ctx['languages'] = Languages.objects.all()

    return TemplateResponse(request, 'sites/home.html', ctx)


def tips(request):
    ctx = {}
    ctx['tips'] = Tip.objects.all()
    ctx['languages'] = Languages.objects.all()

    return TemplateResponse(request, 'sites/tips.html', ctx)
