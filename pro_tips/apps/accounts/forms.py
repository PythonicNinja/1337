# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from urban.apps.user_profiles.models import CUser


class CUserCreationForm(UserCreationForm):
    class Meta:
        model = CUser
        fields = ['username', 'email', ]

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            CUser._default_manager.get(username=username)
        except CUser.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )



