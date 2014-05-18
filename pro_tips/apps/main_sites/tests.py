from django.http import HttpRequest
from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory

# Create your tests here.
from django.core.urlresolvers import resolve
from django.test import TestCase

from pro_tips.apps.main_sites import views
from pro_tips.apps.tips import models


class HomePageTest(TestCase):
    fixtures = ['initial_data.json']

    # Testing url mappings
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)

    def test_home_url_resolves_to_home_page_view(self):
        found = resolve('/home/')
        self.assertEqual(found.func, views.index)

    def test_tips_url_resolves_to_tips_page_view(self):
        found = resolve('/tips/')
        self.assertEqual(found.func, views.tips)

    # Testing contexts of pages
    def test_home_page_returns_correct_html(self):
        response= self.client.get("/")
        self.assertContains( response, '<html>', status_code=200 )

        self.assertTemplateUsed(response, 'sites/home.html')

        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'includes/menu/menu.html')
        self.assertTemplateUsed(response, 'includes/footer/footer.html')


    def test_tips_returns_correct_html(self):
        response= self.client.get("/tips/")
        self.assertContains( response, '<html>', status_code=200 )

        self.assertTemplateUsed(response, 'sites/tips.html')

        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'includes/menu/menu.html')
        self.assertTemplateUsed(response, 'includes/footer/footer.html')



    def test_adding_languages_to_the_context(self):
        client = Client()
        response = client.get('/')

        shortcuts_from_db = [lang.shortcut for lang in response.context['languages']]
        shortcuts_from_variable = [lang[0] for lang in models.SUPPORTED_LANGUAGES]

        self.assertEquals(shortcuts_from_db, shortcuts_from_variable)

    def test_creation_to_add_to_the_context(self):

        models.Languages.objects.create(**{
            'name': 'test',
            'shortcut': 'bar'
        })
        client = Client()
        response = client.get('/')
        shortcuts_from_variable = [lang[0] for lang in models.SUPPORTED_LANGUAGES]
        self.assertEquals(response.context['languages'].count(), len(shortcuts_from_variable) + 1)

    def test_languages_in_the_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/')

        response = views.index(request)

        shortcuts_from_db = [lang.shortcut for lang in response.context_data['languages']]
        shortcuts_from_variable = [lang[0] for lang in models.SUPPORTED_LANGUAGES]

        self.assertEquals(shortcuts_from_db, shortcuts_from_variable)

        models.Languages.objects.create(**{
            'name': 'test',
            'shortcut': 'bar'
        })

        response = views.index(request)

        self.assertEquals(response.context_data['languages'].count(), len(shortcuts_from_variable) + 1)
