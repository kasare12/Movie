from django.db import models
from django.contrib.auth.models import User

class Friend(models.Model):
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    status = models.BooleanField(default=True)
    hobby = models.CharField(max_length = 200, blank = True)
    city = models.CharField(max_length = 50, blank = True)
    state = models.CharField(max_length = 20, blank = True)

    def __str__(self):
        return str(self.friend)

class Movie(models.Model):
    friend = models.ManyToManyField(Friend)
    title = models.CharField(max_length = 200)
    year = models.IntegerField(blank = True)
    genre = models.CharField(max_length = 50, blank = True)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to="movieimage")
    lead_actor_actress = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return str(self.title)
