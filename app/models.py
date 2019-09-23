from django.db import models, IntegrityError
from django.contrib.auth.models import User

class Picture(models.Model):

    user = models.ForeignKey(
        User, on_delete = models.CASCADE
    )

    title = models.CharField(
        max_length = 100
    )
    cover = models.ImageField(
        upload_to = 'images/'
    )

    def __str__(self):
        return f"{self.id}: {self.title}"

    def get_absolute_url(self):
        return reverse("app:see_picture", kwargs={"id": self.id})


class Vote(models.Model):

    class Meta:
        abstract = True
        unique_together = ['user', 'picture']

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )

    picture = models.ForeignKey(
        Picture,
        on_delete = models.CASCADE
    )

    created = models.DateTimeField(
        auto_now_add = True
    )

    @staticmethod
    def see_if_upvoted_or_downvoted(user_instance, picture_instance, klass):
        if klass.objects.filter(
            user = user_instance,
            picture = picture_instance
        ):
            return True
        else:
            return False

    @staticmethod
    def delete_upvote_or_downvote(user_instance, picture_instance, klass):
        instance = klass.objects.filter(
            user = user_instance,
            picture = picture_instance
        )
        instance.delete()

    @staticmethod
    def create_upvote_or_downvote(user_instance, picture_instance, klass):
        try:
            klass.objects.create(
                user = user_instance,
                picture = picture_instance
            )
            return True
        except IntegrityError:
            Upvote.delete_upvote_or_downvote(user_instance, picture_instance, klass)

    @staticmethod
    def vote(user_instance, picture_instance, klass):
        if isinstance(klass, Upvote):
            if Downvote.see_if_upvoted_or_downvoted(user_instance, picture_instance, Downvote):
                Downvote.delete_upvote_or_downvote(user_instance, picture_instance, Downvote)
                Upvote.create_upvote_or_downvote(user_instance, picture_instance, Upvote)
            else:
                Upvote.create_upvote_or_downvote(user_instance, picture_instance, Upvote)
        elif isinstance(klass, Downvote):
            if Upvote.see_if_upvoted_or_downvoted(user_instance, picture_instance, Upvote):
                Upvote.delete_upvote_or_downvote(user_instance, picture_instance, Upvote)
                Downvote.create_upvote_or_downvote(user_instance, picture_instance, Downvote)
            else:
                Downvote.create_upvote_or_downvote(user_instance, picture_instance, Downvote)

class Upvote(Vote):
    def __str__(self):
        return f"{self.user.username} upvoted {self.picture} on {self.created}."

class Downvote(Vote):
    def __str__(self):
        return f"{self.user.username} downvoted {self.picture} on {self.created}."






