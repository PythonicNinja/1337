from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from pro_tips.apps.accounts.models import CUser

from pro_tips.apps.api import views
from pro_tips.apps.tips.models import Tip, Languages

# ^api/ ^tips/$ [name='tips_list']
# ^api/ ^languages/$ [name='languages_list']
# ^api/ ^tip/comments/$ [name='comment_for_tip']
# ^api/ ^tip/votes/(?P<tip>\d*)/$ [name='votes_for_tip']
# ^api/ ^comment/add/$ [name='add_comment']
# ^api/ ^tips/logged/$ [name='tips_logged']
# ^api/ ^tips/votes/logged/$ [name='tips_votes']
# ^api/ ^tip/favourites/logged/$ [name='favourites_for_tip']
# ^api/ ^languages/logged/$ [name='languages_logged']
class ApiTest(TestCase):
    fixtures = ['initial_data.json']

    def test_list_tips_url_resolves_to_list_tips_view(self):
        found = resolve('/api/tips/')
        self.assertEqual(found.func.__name__, views.TipsList.as_view().__name__)

    # Testing url mappings
    def test_languages_list_url_resolves_to_list_languages_view(self):
        found = resolve('/api/languages/')
        self.assertEqual(found.func.__name__,
                         views.LanguagesList.as_view().__name__)

    def test_list_comments_url_resolves_to_list_comments_view(self):
        found = resolve('/api/tip/comments/')
        self.assertEqual(found.func.__name__,
                         views.CommentsList.as_view().__name__)

    def test_list_comments_url_resolves_to_list_tips_logged_view(self):
        found = resolve('/api/tips/logged/')
        self.assertEqual(found.func.__name__, views.TipsView.as_view().__name__)

    def test_list_comments_url_resolves_to_votes_view(self):
        found = resolve('/api/tips/votes/logged/')
        self.assertEqual(found.func.__name__,
                         views.VotesView.as_view().__name__)

    def test_list_comments_url_resolves_to_favourite_view(self):
        found = resolve('/api/tip/favourites/logged/')
        self.assertEqual(found.func.__name__,
                         views.FavouriteView.as_view().__name__)

    def test_list_comments_url_resolves_to_languages_view(self):
        found = resolve('/api/languages/logged/')
        self.assertEqual(found.func.__name__,
                         views.LanguagesView.as_view().__name__)

    # Status 200 test unauthenticated views
    def test_200_tips_list(self):
        response = self.client.get(reverse('api:tips_list'))
        self.assertEqual(response.status_code, 200)

    def test_200_languages_list(self):
        response = self.client.get(reverse('api:languages_list'))
        self.assertEqual(response.status_code, 200)

    # Testing contents of api


