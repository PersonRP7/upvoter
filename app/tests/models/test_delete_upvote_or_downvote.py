from .test_setup import TestSetUpClass
from app.models import Upvote, Downvote


class TestVoteSetUp(TestSetUpClass):

    def create_vote(self, klass):
        klass.objects.create(
            user = self.user,
            picture = self.picture
        )

class TestDeleteUpvote(TestVoteSetUp):

    def setUp(self):
        super().setUp()
        self.create_vote(Upvote)
        self.create_vote(Downvote)
        
    def test_upvote_present(self):
        self.assertTrue(
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

    def test_downvote_deleted(self):
        Downvote.delete_upvote_or_downvote(
            self.user, self.picture, Downvote
        )
        self.assertFalse(
            Downvote.objects.filter(
                user = self.user
            )
        )

    def test_upvote_deleted(self):
        Upvote.delete_upvote_or_downvote(
            self.user, self.picture, Upvote
        )
        self.assertFalse(
            Upvote.objects.filter(
                user = self.user
            )
        )

    

    
    
