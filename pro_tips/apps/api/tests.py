from django.test import TestCase, Client
from django.test import TestCase, RequestFactory
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

    def setUp(self):
        self.lang = Languages.objects.get(id=1)
        self.user = CUser.objects.create_user(
            username='joedoe', password='top_secret')
        self.tip = Tip.objects.create(user=self.user, title="asd",
                                      description="asd", language=self.lang)

    def login(self):
        self.client = Client()
        self.user = CUser.objects.create_user('test', 'test@test.com', 'test')
        self.client.login(username='test', password='test')

    # url mappings
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

    def test_200_api_tips_logged(self):
        self.client.login( username='joedoe', password='top_secret')
        response = self.client.get(reverse('api:tips_logged'))
        self.assertEqual(response.status_code, 200)

    def test_200_api_votes_for_tip(self):
        self.client.login(username='joedoe', password='top_secret')
        response = self.client.get(reverse('api:votes_for_tip', kwargs={'tip': self.tip.pk}))
        self.assertEqual(response.status_code, 200)

    def test_200_tips_logged(self):
        self.client.login(username='joedoe', password='top_secret')
        response = self.client.get(reverse('api:tips_logged'))
        self.assertEqual(response.status_code, 200)

    def test_200_tips_votes(self):
        self.client.login(username='joedoe', password='top_secret')
        response = self.client.get(reverse('api:tips_votes'))
        self.assertEqual(response.status_code, 200)

    def test_200_favourites_for_tip(self):
        self.client.login(username='joedoe', password='top_secret')
        response = self.client.get(reverse('api:favourites_for_tip'))
        self.assertEqual(response.status_code, 200)

    def test_200_languages_logged(self):
        self.client.login(username='joedoe', password='top_secret')
        response = self.client.get(reverse('api:languages_logged'))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.user.delete()
        self.tip.delete()

    def test_302_add_comment(self):
        response = self.client.get(reverse('api:add_comment'))
        #redirect to login page
        self.assertEqual(response.status_code, 302)

    # Status 403 test authenticated views without login
    def test_403_tips_logged(self):
        response = self.client.get(reverse('api:tips_logged'))
        self.assertEqual(response.status_code, 403)

    def test_403_tips_votes(self):
        response = self.client.get(reverse('api:tips_votes'))
        self.assertEqual(response.status_code, 403)

    def test_403_favourites_for_tip(self):
        response = self.client.get(reverse('api:favourites_for_tip'))
        self.assertEqual(response.status_code, 403)

    def test_403_languages_logged(self):
        response = self.client.get(reverse('api:languages_logged'))
        self.assertEqual(response.status_code, 403)

    # Status 200 test authenticated views with login
    def test_200_add_comment(self):
        self.login()
        response = self.client.get(reverse('api:add_comment'))
        self.assertEqual(response.status_code, 200)


    # Testing contents of api


