import pickle
import os
import logging

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from pro_tips.apps.tips.models import Vote, Tip, Languages
from pro_tips.apps.accounts.models import CUser

__author__ = 'sebnapi'

logger = logging.getLogger("apps.tips")


class Command(BaseCommand):
    args = 'no args'
    help = 'loads default tips into database'

    def handle(self, *args, **options):

        with open(os.path.join(os.getcwd(), "apps/tips/fixtures/markdown_snippets_dict.pickle")) as f:
            snippets_dict = pickle.load(f)

        try:
            robot = self.__create_useless_user("iRobot")
        except IntegrityError:
            robot = CUser.objects.get(username="iRobot")
        except:
            logger.error("Cannot create iRobot User for default tips")
            return

        users = self.__create_vote_users(10)

        for k,v in snippets_dict.items():
            try:
                lang = Languages.objects.get(name=k)
            except:
                logger.error("No Language found with name %s" % k)
                continue

            for s in v:
                tip = Tip.objects.create(user=robot, title=s["title"], description=s["body"][1], language=lang)
                self.__cast_dumb_votes(tip, int(s["votes"]), users)


    def __cast_dumb_votes(self, tip, amount, users):
        for i in xrange(0, min(abs(amount), len(users))):
            if amount < 0:
                tip.vote_down(users[i])
            elif amount > 0:
                tip.vote_up(users[i])



    def __create_vote_users(self, amount):
        users = []
        for i in xrange(0, amount):
            try:
                user = self.__create_useless_user("DumbVoteUser%s" % i)
                users.append(user)
            except IntegrityError:
                try:
                    user = CUser.objects.get(name="DumbVoteUser%s" % i)
                    users.append(user)
                except:
                    pass
            except:
                continue
        return users

    def __create_useless_user(self, name):
        user = CUser.objects.create(username=name, password="123")
        user.set_unusable_password()
        user.is_active = False
        user.save()
        return user