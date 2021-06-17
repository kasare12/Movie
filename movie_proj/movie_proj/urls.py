"""movie_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from movieApp import views
from commentsApp.views import CommentCreateView
from movieApp.views import ( 
    MovieListView, 
    FriendListView,
    MovieCreateView,
    MovieUpdateView,
    MovieDetailView,
    SignUpView,
    FriendDetailView,
    MovieMyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MovieListView.as_view(), name="movie_list"),
    path('friends/', FriendListView.as_view(), name="friend_list"),
    path('addmovie/', MovieCreateView.as_view(), name="movie_create"),
    path('updatemovie/<int:pk>/', MovieUpdateView.as_view(), name="movie_update"),
    path('moviedetail/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('frienddetail/<int:pk>/', FriendDetailView.as_view(), name="friend_detail"),
    path('moviemyview/', MovieMyView.as_view(), name="movie_myview"),
    path('createcomment/<movie>/', CommentCreateView.as_view(), name="create_comment"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

