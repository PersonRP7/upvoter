from django.test import TestCase
import json
from app.helpers import login_to_vote

class TestLoginToVote(TestCase):

    def test_login_to_vote(self):
        response = login_to_vote()
        content = json.loads(response.content)
        error = content["error"]
        self.assertEqual(
            response.status_code,
            401
        )
        self.assertEqual(
            error,
            "Log in to vote."
        )