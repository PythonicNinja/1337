# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages
from django.template.response import TemplateResponse


from pro_tips.apps.accounts.forms import CUserCreationForm
from django.contrib.auth import authenticate, login


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
        user = registration_form.save()
        log_in_user = authenticate(username=user.username,
                                    password=request.POST['password2'])
        login(request,log_in_user)
        return redirect("accounts:user-profile")
    context.update({
        'form': registration_form,
    })
    return TemplateResponse(request, 'user_profiles/sites/registration.html', context)



