from .test_setup import TestSetup
from app.helpers import vote_action
from app.models import Upvote, Downvote
import json

class TestVoteActionUpvote(TestSetup):


    def test_vote_action_upvote(self):
        value = vote_action(self.user, self.picture1, Upvote)
        content = json.loads(value.content)
        upvotes = content["upvotes"]
        downvotes = content["downvotes"]
        success = content["success"]
        self.assertEqual(
            value.status_code,
            200
        )
        self.assertEqual(
            upvotes, 1
        )
        self.assertEqual(
            downvotes, 0
        )
        self.assertEqual(
            success, True
        )


class TestVoteActionDownvote(TestSetup):

    def test_vote_action_upvote(self):
        value = vote_action(self.user, self.picture1, Downvote)
        content = json.loads(value.content)
        upvotes = content["upvotes"]
        downvotes = content["downvotes"]
        success = content["success"]
        self.assertEqual(
            value.status_code,
            200
        )
        self.assertEqual(
            upvotes, 0
        )
        self.assertEqual(
            downvotes, 1
        )
        self.assertEqual(
            success, True
        )



