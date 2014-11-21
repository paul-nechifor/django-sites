from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for quesitons whose pub_date
        is in the future.
        """
        future_time = timezone.now() + timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertEqual(future_question.was_published_recently(), False)
