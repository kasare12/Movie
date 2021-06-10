from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie, Friend

class MovieListView(ListView):
    model = Movie

class FriendListView(ListView):
    model = Friend