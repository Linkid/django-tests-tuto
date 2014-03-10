from django.test import TestCase
from django.utils.timezone import utc
from myapp.models import Poll, Choice

import datetime


class TestPollModel(TestCase):
    def setUp(self):
        ## First poll
        self.first_question = "What is your age?"
        self.first_date = datetime.datetime(2014, 3, 11, 0, 1).replace(tzinfo=utc)

        first_poll = Poll()
        first_poll.question = self.first_question
        first_poll.pub_date = self.first_date
        first_poll.save()

    def test_poll(self):
        ## Get all polls and the first one
        saved_polls = Poll.objects.all()
        first_saved_poll = saved_polls[0]

        self.assertEquals(saved_polls.count(), 1)
        self.assertEquals(first_saved_poll.question, self.first_question)
        self.assertEquals(first_saved_poll.pub_date, self.first_date)

    def test_choice(self):
        first_choice = Choice()
        first_choice.poll = Poll.objects.first()
        first_choice.save()

        saved_choices = Choice.objects.all()
        first_saved_choice = saved_choices[0]

        self.assertEquals(saved_choices.count(), 1)
        self.assertEquals(first_saved_choice.poll, Poll.objects.first())
