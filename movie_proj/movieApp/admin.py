from django.contrib import admin
from .models import Movie, Friend

admin.site.register(Movie)
admin.site.register(Friend)

# class MovieInLine(admin.TabularInline):
#     model = Movie
#     extra = 1

# class FriendAdmin(admin.ModelAdmin):
#     inlines = [MovieInLine]
#     listdisplay = ["__str__"]
#     class Meta:
#         model = Friend

# admin.site.register(Friend, FriendAdmin)

