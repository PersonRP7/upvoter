from django.db import IntegrityError
from .models import Upvote, Downvote
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from .models import Picture

def get_votes(klass, instance):
    return klass.objects.filter(picture = instance).count()


def return_json(up_klass, down_klass, status_boolean):
    return JsonResponse({
        "success":status_boolean,
        "upvotes":up_klass,
        "downvotes":down_klass
    }, status = 200)

def login_to_vote():
    return JsonResponse({
        "error":"Log in to vote."
    }, status = 401)

#Calls get_votes and return_json
def vote_action(user, instance, upvote_or_downvote):
    try:
        upvote_or_downvote.vote(user, instance, upvote_or_downvote())
        upvotes = get_votes(Upvote, instance)
        downvotes = get_votes(Downvote, instance)
        return return_json(upvotes, downvotes, True)
    except IntegrityError:
        upvotes = get_votes(Upvote, instance)
        downvotes = get_votes(Downvote, instance)
        return return_json(upvotes, downvotes, False)
    except TypeError:
        return login_to_vote()

def seek_instance(instance, gt_or_lt, pk):
    try:
        inst = Picture.objects.filter(**{f"id__{gt_or_lt}":instance.id}).order_by(pk).first()
        return reverse("app:see_picture", kwargs={"id":inst.id})
    except AttributeError:
        return reverse("app:see_picture", kwargs={'id':instance.id})


