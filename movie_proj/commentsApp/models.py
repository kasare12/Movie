from django.db import models
from django.contrib.auth.models import User
from movieApp.models import Movie

class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField(max_length = 600)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} , {}".format(self.title, self.username)
