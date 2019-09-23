from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect
from .models import Picture, Upvote, Downvote
from . forms import PictureForm
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from . import helpers
from django.http import JsonResponse

def home(request):
    return render(request, 'app/home.html')

def live(request):
    return render(request, 'app/live.html')

@login_required
def create_picture(request, id = None):
    if request.method == 'GET':
        form = PictureForm()
        return render(request, 'app/create_picture.html', {'form':form})
    else:
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            messages.info(request, "Picture saved.")
            return HttpResponseRedirect(
                reverse('app:see_picture', kwargs = {'id':instance.id})
            )
        else:
            messages.info(request, "Form not correct.")
            return render(request, "app/create_picture.html", {'form':form})

def see_picture(request, id = None):
    instance = get_object_or_404(Picture, id = id)
    previous = helpers.seek_instance(instance, "lt", "-pk")
    following = helpers.seek_instance(instance, "gt", "pk")
    upvote_count = instance.upvote_set.all().count()
    downvote_count = instance.downvote_set.all().count()

    return render(
        request, 'app/see_picture.html',
        {
            'instance':instance,
            'previous':previous,
            'following':following,
            'upvote_count':upvote_count,
            'downvote_count':downvote_count
        }
    )

@require_POST
def upvote(request, id = None):
    picture = get_object_or_404(Picture, id = id)
    user = request.user
    return helpers.vote_action(user, picture, Upvote)

@require_POST
def downvote(request, id = None):
    picture = get_object_or_404(Picture, id = id)
    user = request.user
    return helpers.vote_action(user, picture, Downvote)

@require_GET
def get_votes_count(request, id = None):
    upvotes = helpers.vote_count("upvote", id = id)
    downvotes = helpers.vote_count("downvote", id = id)
    return JsonResponse({
        "upvotes":upvotes,
        "downvotes":downvotes
    }, status = 200)






