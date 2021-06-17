from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView 
from django.urls import reverse_lazy
from .models import Movie, Friend
from .forms import SignUpForm
from django.shortcuts import get_object_or_404
from commentsApp.models import Comment
from django.views import View

class MovieListView(ListView):
    model = Movie

class MovieMyView(View):
    def get(self, request):
        movies = Movie.objects.all()

        return render(request, 'movieApp/movie_myview.html', {'movies': movies})

class FriendListView(ListView):
    model = Friend

class FriendDetailView(DetailView):
    model = Friend

    def get_context_data(self, *args, **kwargs):
        context = super(FriendDetailView, self).get_context_data(**kwargs)
        # print(context)
        context["movies"] = Movie.objects.filter(friend__id=self.kwargs["pk"])
        context["comments"] = Comment.objects.filter(username=self.object.friend)
        print(context)

        return context

class MovieCreateView(CreateView):
    model = Movie
    fields = ['title','year','genre','description','image','lead_actor_actress']
    success_url = reverse_lazy('movie_list')

class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['title','year','genre','description','image','lead_actor_actress']
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('movie_list')

class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, *args, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context["friends"] = Friend.objects.filter(movie__id=self.kwargs["pk"])
        # print("->>>>>" , self.object.genre)
        context["genres"] = Movie.objects.filter(genre=self.object.genre)
        context["comments"] = Comment.objects.filter(title__id=self.kwargs["pk"])
        print(context)

        return context

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'movieApp/signup.html'
    success_url = reverse_lazy('movie_list')