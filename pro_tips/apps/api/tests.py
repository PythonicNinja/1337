from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from pro_tips.apps.accounts.models import CUser

from pro_tips.apps.api import views
from pro_tips.apps.tips.models import Tip, Languages

# Create your tests here.
class ApiTest(TestCase):
    fixtures = ['initial_data.json']

    # Testing url mappings
    def test_languages_list_url_resolves_to_list_languages_view(self):
        found = resolve('/api/languages/')
        self.assertEqual(found.func.__name__,
                         views.LanguagesList.as_view().__name__)

    def test_list_tips_url_resolves_to_list_tips_view(self):
        found = resolve('/api/tips/')
        self.assertEqual(found.func.__name__, views.TipsList.as_view().__name__)

    def test_list_comments_url_resolves_to_list_comments_view(self):
        found = resolve('/api/tip/comments/')
        self.assertEqual(found.func.__name__,
                         views.CommentsList.as_view().__name__)


    # Status 200 test unauthenticated views
    def test_200_tips_list(self):
        response = self.client.get(reverse('api:tips_list'))
        self.assertEqual(response.status_code, 200)

    def test_200_languages_list(self):
        response = self.client.get(reverse('api:languages_list'))
        self.assertEqual(response.status_code, 200)

    # Testing contents of api


