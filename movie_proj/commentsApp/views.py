from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from movieApp.models import Movie
from .models import Comment

class CommentCreateView(CreateView):
    model = Comment
    fields = ['username','title','review']
    success_url = reverse_lazy('movie_detail')
    # print("->>>>>>", success_url)

