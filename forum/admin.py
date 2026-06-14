from django.contrib import admin
from .models import Thread, Comment


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "date_posted"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["__str__", "author", "thread", "date_posted"]