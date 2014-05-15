from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.template.response import TemplateResponse


def index(request):
    ctx = {}

    return TemplateResponse(request, 'sites/home.html', ctx)
