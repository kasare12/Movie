from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created",)

admin.site.register(Comment,CommentAdmin)
