from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from . forms import SearchForm

def search_main(request):
    if request.method == 'GET':
        form = SearchForm()
        return render(
            request, 'search/search_main.html',
            {'form':form}
        )
    elif request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            pass


