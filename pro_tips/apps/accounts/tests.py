"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client
from django.core.urlresolvers import resolve, reverse

from django.contrib.auth import views as django_views

from pro_tips.apps.accounts import views
from pro_tips.apps.accounts.models import CUser


class AccountsTests(TestCase):

    def login(self):
        self.client = Client()
        self.user = CUser.objects.create_user('test', 'test@test.com', 'test')
        self.client.login(username='test', password='test')

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


    # Testing contexts of pages
    def test_register_page_returns_correct_html(self):
        response= self.client.get(reverse('accounts:register'))
        self.assertContains( response, '<html>', status_code=200)
        self.assertTemplateUsed(response, 'user_profiles/sites/registration.html')

    def test_footer_page_register(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertTemplateUsed(response, 'includes/footer/footer.html')

    def test_menu_page_register(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertTemplateUsed(response, 'includes/menu/menu.html')

    def test_extends_base_html_page_register(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertTemplateUsed(response, 'base.html')


    def test_profile_page_returns_correct_html(self):
        self.login()
        response = self.client.get(reverse('accounts:user-profile'))
        self.assertContains( response, '<html>', status_code=200)
        self.assertTemplateUsed(response, 'user_profiles/sites/user_profile.html')

    def test_footer_page_profile(self):
        self.login()
        response = self.client.get(reverse('accounts:user-profile'))
        self.assertTemplateUsed(response, 'includes/footer/footer.html')

    def test_menu_page_profile(self):
        self.login()
        response = self.client.get(reverse('accounts:user-profile'))
        self.assertTemplateUsed(response, 'includes/menu/menu.html')

    def test_extends_base_html_page_profile(self):
        self.login()
        response = self.client.get(reverse('accounts:user-profile'))
        self.assertTemplateUsed(response, 'base.html')




