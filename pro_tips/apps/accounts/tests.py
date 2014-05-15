"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse

from django.contrib.auth import views as django_views

from pro_tips.apps.accounts import views


class AccountsTests(TestCase):

    # Status 200 test views
    # TODO: add more test like 200
    def test_200_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_200_tips(self):
        response = self.client.get(reverse('tips'))
        self.assertEqual(response.status_code, 200)

    # Testing url mappings
    def test_login_url_resolves_to_login_view(self):
        found = resolve('/accounts/login/')
        self.assertEqual(found.func.__name__, django_views.login.__name__)
