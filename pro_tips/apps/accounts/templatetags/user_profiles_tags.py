from django import template
from django.contrib.auth.forms import AuthenticationForm

from pro_tips.apps.accounts.forms import CUserCreationForm

register = template.Library()


@register.inclusion_tag('user_profiles/includes/login.html')
def login_tag(user):
    form_login = AuthenticationForm()
    form_register = CUserCreationForm()
    return {"form_login":form_login,'form_register':form_register, 'user':user }
