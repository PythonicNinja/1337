from django.test import TestCase
from pro_tips.apps.accounts.models import CUser
from pro_tips.apps.tips.models import Vote, Tip, Languages


class TipsTest(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.user = CUser.objects.create(username='user')
        self.user1 = CUser.objects.create(username='user1')
        self.user2 = CUser.objects.create(username='user2')
        lang = Languages.objects.get(id=1)
        self.tip = Tip.objects.create(user=self.user, title="Test1", description="Test Descr", language=lang)

    def test_tip_vote_two_times(self):
        """
        User is trying to vote two times the same vote
        this is not allowed
        """

        vote1 = Vote.objects.create(type=True, user=self.user, tip=self.tip)
        vote2 = Vote.objects.create(type=True, user=self.user, tip=self.tip)
        self.assertTrue(self.tip.vote_set.count() == 1)

    def test_tip_change_vote(self):
        """
        User is trying to cast an other vote
        this is allowed, the existing vote gets updated
        """

        Vote.objects.create(type=True, user=self.user, tip=self.tip)

        self.assertTrue(self.tip.vote_set.count() == 1)

        voteFromDb = self.tip.vote_set.iterator().next()

        self.assertTrue(voteFromDb.type is True)
        self.assertTrue(voteFromDb.user == self.user)
        self.assertTrue(voteFromDb.tip == self.tip)

        Vote.objects.create(type=False, user=self.user, tip=self.tip)

        self.assertTrue(self.tip.vote_set.count() == 1, msg="Vote count should not be changed.")

        voteFromDb = self.tip.vote_set.iterator().next()

        self.assertTrue(voteFromDb.type is False, msg="Vote should be changed.")
        self.assertTrue(voteFromDb.user == self.user)
        self.assertTrue(voteFromDb.tip == self.tip)

    def test_vote_rating(self):
        """
        Tests the get_rating_by_tip method
        """

        Vote.objects.create(type=True, user=self.user, tip=self.tip)

        self.assertTrue(self.tip.get_rating() == 1)

        Vote.objects.create(type=True, user=self.user1, tip=self.tip)

        self.assertTrue(self.tip.get_rating() == 2)

        Vote.objects.create(type=False, user=self.user2, tip=self.tip)

        self.assertTrue(self.tip.get_rating() == 1)


    def tearDown(self):
        Vote.objects.all().delete()
        self.user.delete()
        self.tip.delete()