from .test_setup import TestSetUpClass
from app.models import Upvote, Downvote

class TestSeeIfUpvotedOrDownvotedFalse(TestSetUpClass):

    def setUp(self):
        super().setUp()

    def test_upvote_returns_false(self):
        value = Upvote.see_if_upvoted_or_downvoted(
            self.user, self.picture, Upvote
        )
        self.assertFalse(
            value
        )

    def test_downvote_returns_false(self):
        value = Downvote.see_if_upvoted_or_downvoted(
            self.user, self.picture, Downvote
        )
        self.assertFalse(
            value
        )

class TestSeeIfUpvotedOrDownvotedTrue(TestSetUpClass):

    def setUp(self):
        super().setUp()
        Upvote.objects.create(
            user = self.user,
            picture = self.picture
        )
        Downvote.objects.create(
            user = self.user,
            picture = self.picture
        )

    def test_upvote_returns_true(self):
        value = Upvote.see_if_upvoted_or_downvoted(
            self.user, self.picture, Upvote
        )
        self.assertTrue(
            value
        )

    def test_downvote_returns_true(self):
        value = Downvote.see_if_upvoted_or_downvoted(
            self.user, self.picture, Downvote
        )
        self.assertTrue(
            value
        )
    