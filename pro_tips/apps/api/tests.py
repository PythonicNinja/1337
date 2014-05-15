from django.test.client import Client
from django.test.client import RequestFactory
from django.core.urlresolvers import resolve
from django.test import TestCase

from pro_tips.apps.api import views

# Create your tests here.
class ApiTest(TestCase):

    # Testing url mappings
    def test_languages_list_url_resolves_to_list_languages_view(self):
        found = resolve('/api/languages/')
        self.assertEqual(found.func.__name__, views.ListLanguages.as_view().__name__)


    # Testing contents of api
