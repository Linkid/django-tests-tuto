from django.test import TestCase
from django.utils.timezone import utc
from myapp.models import Poll

import datetime


class TestPollModel(TestCase):
    def test_poll(self):
        first_poll = Poll()
        first_question = "What is your age?"
        first_date = datetime.datetime(2014, 3, 11, 0, 1).replace(tzinfo=utc)
        first_poll.question = first_question
        first_poll.pub_date = first_date
        first_poll.save()

        saved_polls = Poll.objects.all()
        first_saved_poll = saved_polls[0]

        self.assertEquals(saved_polls.count(), 1)
        self.assertEquals(first_saved_poll.question, first_question)
        self.assertEquals(first_saved_poll.pub_date, first_date)
