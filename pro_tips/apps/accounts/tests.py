"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve

from django.contrib.auth import views as django_views

from pro_tips.apps.accounts import views


class AccountsTests(TestCase):

    # Testing url mappings
    def test_login_url_resolves_to_login_view(self):
        found = resolve('/accounts/login/')
        self.assertEqual(found.func.__name__, django_views.login.__name__)
