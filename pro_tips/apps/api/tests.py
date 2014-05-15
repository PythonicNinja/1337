from django.test import TestCase
from django.core.urlresolvers import resolve

from pro_tips.apps.api import views

# Create your tests here.
class ApiTest(TestCase):

    # Testing url mappings
    def test_languages_list_url_resolves_to_list_languages_view(self):
        found = resolve('/api/languages/')
        self.assertEqual(found.func.__name__, views.LanguagesList.as_view().__name__)

    def test_list_tips_url_resolves_to_list_tips_view(self):
        found = resolve('/api/tips/')
        self.assertEqual(found.func.__name__, views.TipsList.as_view().__name__)

    def test_list_comments_url_resolves_to_list_comments_view(self):
        found = resolve('/api/tip/comments/')
        self.assertEqual(found.func.__name__, views.CommentsList.as_view().__name__)


    # Testing contents of api
