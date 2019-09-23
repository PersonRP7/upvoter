from .test_create_upvote_or_downvote import TestTransactionSetup
from app.models import Upvote, Downvote, Picture

class TestUpvoteExists(TestTransactionSetup):

    def setUp(self):
        super().setUp()
        Upvote.vote(
            self.user, self.picture, Upvote()
        )

    def test_upvote_exists(self):
        self.assertTrue(
            Upvote.objects.filter(
                user = self.user
            )
        )

class DownvoteExists(TestTransactionSetup):

    def setUp(self):
        super().setUp()
        Downvote.vote(
            self.user, self.picture, Downvote()
        )

    def test_downvote_exists(self):
        self.assertTrue(
            Downvote.objects.filter(
                user = self.user
            )
        )

class TestDownvoteCancelledOut(TestTransactionSetup):

    def setUp(self):
        super().setUp()
        Downvote.vote(
            self.user, self.picture, Downvote()
        )
        Upvote.vote(
            self.user, self.picture, Upvote()
        )

    def test_downvote_cancelled_out(self):
        self.assertFalse(
            Downvote.objects.filter(
                user = self.user
            )
        )

    def test_upvote_present(self):
        self.assertTrue(
            Upvote.objects.filter(
                user = self.user
            )
        )

class TestUpvoteCancelledOut(TestTransactionSetup):

    def setUp(self):
        super().setUp()
        Upvote.vote(
            self.user, self.picture, Upvote()
        )
        Downvote.vote(
            self.user, self.picture, Downvote()
        )

    def test_upvote_cancelled_out(self):
        self.assertFalse(
            Upvote.objects.filter(
                user = self.user
            )
        )

    def test_downvote_present(self):
        self.assertTrue(
            Downvote.objects.filter(
                user = self.user
            )
        )

class DownvoteCancelsDownvote(TestTransactionSetup):

    def setUp(self):
        super().setUp()
        Downvote.vote(
            self.user, self.picture, Downvote()
        )
        Downvote.vote(
            self.user, self.picture, Downvote()
        )

    def test_downvote_cancelled_out(self):
        self.assertFalse(
            Downvote.objects.filter(
                user = self.user
            )
        )

class TestUpvoteCancelsUpvote(TestTransactionSetup):

    def setUp(self):
        super().setUp()
        Upvote.vote(
            self.user, self.picture, Upvote()
        )
        Upvote.vote(
            self.user, self.picture, Upvote()
        )

    def test_upvote_cancelled_out(self):
        self.assertFalse(
            Upvote.objects.filter(
                user = self.user
            )
        )