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
    def test_200_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_200_tips(self):
        response = self.client.get(reverse('tips'))
        self.assertEqual(response.status_code, 200)

    def test_200_registration(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)

    def test_200_pwd_change_done(self):
        response = self.client.get(reverse('accounts:password_reset_done'))
        self.assertEqual(response.status_code, 200)

    def test_302_logout(self):
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)

    def test_302_pwd_change(self):
        response = self.client.get(reverse('accounts:pwd-change'))
        self.assertEqual(response.status_code, 302)

    # Testing url mappings
    def test_login_url_resolves_to_login_view(self):
        found = resolve('/accounts/login/')
        self.assertEqual(found.func.__name__, django_views.login.__name__)
