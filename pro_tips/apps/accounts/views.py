# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages
from django.template.response import TemplateResponse


from pro_tips.apps.accounts.forms import CUserCreationForm


###PROFILE

def user_profile(request):
    context = {

    }
    return TemplateResponse(request, 'user_profiles/sites/user_profile.html',context)



##AUTH
def registration(request):
    context = {}

    registration_form = CUserCreationForm(request.POST or None)
    if registration_form.is_valid():
        return redirect("main")
    context.update({
        'form': registration_form,
    })
    return TemplateResponse(request, 'user_profiles/sites/registration.html', context)



