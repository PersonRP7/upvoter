from .test_setup import TestSetUpClass
from django.test import TransactionTestCase
from django.core.files.base import File
from app.models import Upvote, Downvote, Picture, User


class TestTransactionSetup(TransactionTestCase):

    def create_user(self):
        User.objects.create_user(
            username = "admin",
            password = "testing321"
        )

    # def create_upvote(self):
    #     Upvote.vote(
    #         self.user, self.picture, Upvote()
    #     )

    # def create_downvote(self):
    #     Downvote.vote(
    #         self.user, self.picture, Downvote()
    #     )

    def create_picture(self):
        Picture.objects.create(
            user = User.objects.get(username = "admin"),
            title = "Picture One",
            cover = File(file=b"")
        )

    def setUp(self):
        self.create_user()
        self.create_picture()
        self.user = User.objects.get(
            username = "admin"
        )
        self.picture = Picture.objects.get(
            title = "Picture One"
        )

class TestDownvoteTransaction(TestTransactionSetup):

    def setUp(self):
        super().setUp()
        Downvote.create_upvote_or_downvote(
            self.user, self.picture, Downvote
        )

    def test_downvote_deleted(self):
        Downvote.create_upvote_or_downvote(
            self.user, self.picture, Downvote
        )
        self.assertFalse(
            Downvote.objects.filter(
                user = self.user
            )
        )

class TestUpvoteTransaction(TestTransactionSetup):

    def setUp(self):
        super().setUp()
        Upvote.create_upvote_or_downvote(
            self.user, self.picture, Upvote
        )

    def test_upvote_deleted(self):
        Upvote.create_upvote_or_downvote(
            self.user, self.picture, Upvote
        )
        self.assertFalse(
            Upvote.objects.filter(
                user = self.user
            )
        )
        


class TestUpvote(TestSetUpClass):

    def test_upvote_not_present(self):
        self.assertFalse(
            Upvote.objects.filter(
                user = self.user
            )
        )

    def test_create_upvote_returns_true(self):
        value = Upvote.create_upvote_or_downvote(
            self.user, self.picture, Upvote
        )
        self.assertTrue(
            value
        )
        self.assertTrue(
            Upvote.objects.filter(
                user = self.user
            )
        )

class TestDownvote(TestSetUpClass):

    def test_downvote_not_present(self):
        self.assertFalse(
            Downvote.objects.filter(
                user = self.user
            )
        )

    def test_create_downvote_returns_true(self):
        value = Downvote.create_upvote_or_downvote(
            self.user, self.picture, Downvote
        )
        self.assertTrue(
            value
        )
        self.assertTrue(
            Downvote.objects.filter(
                user = self.user
            )
        )

    