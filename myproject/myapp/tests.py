from django.test import TestCase
from django.utils.timezone import utc
from myapp.models import Poll, Choice

import datetime


class TestPollModel(TestCase):
    def setUp(self):
        ## First poll
        self.first_question = "What is your age?"
        self.first_date = datetime.datetime.now().replace(tzinfo=utc)
        self.first_choice_text = "42"
        self.second_date = datetime.datetime(2014, 1, 11, 0, 1).replace(tzinfo=utc)

        first_poll = Poll()
        first_poll.question = self.first_question
        first_poll.pub_date = self.first_date
        first_poll.save()

        second_poll = Poll()
        second_poll.question = self.first_question
        second_poll.pub_date = self.second_date
        second_poll.save()

        first_choice = Choice()
        first_choice.poll = Poll.objects.all()[0]
        first_choice.choice_text = self.first_choice_text
        first_choice.save()

    def test_poll_saved(self):
        ## Get all polls and the first one
        saved_polls = Poll.objects.all()
        first_saved_poll = saved_polls[0]

        self.assertEquals(saved_polls.count(), 2)
        self.assertEquals(first_saved_poll.question, self.first_question)
        self.assertEquals(first_saved_poll.pub_date, self.first_date)

    def test_poll_unicode(self):
        first_saved_poll = Poll.objects.all()[0]
        self.assertEquals(str(first_saved_poll), self.first_question)

    def test_poll_recently_pulished(self):
        first_saved_poll = Poll.objects.all()[0]
        self.assertTrue(first_saved_poll.was_published_recently())

    def test_poll_not_recently_pulished(self):
        second_saved_poll = Poll.objects.all()[1]
        self.assertFalse(second_saved_poll.was_published_recently())

    def test_choice_saved(self):
        saved_choices = Choice.objects.all()
        first_saved_choice = saved_choices[0]
        first_poll_linked = Poll.objects.all()[0]

        self.assertEquals(saved_choices.count(), 1)
        self.assertEquals(first_saved_choice.poll, first_poll_linked)
        self.assertEquals(first_saved_choice.choice_text, self.first_choice_text)
        self.assertEquals(first_saved_choice.votes, 0)
        self.assertEquals(first_poll_linked.choice_set.count(), 1)

    def test_choice_unicode(self):
        first_saved_choice = Choice.objects.all()[0]
        self.assertEquals(str(first_saved_choice), self.first_choice_text)

