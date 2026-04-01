from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post


class BlogListView(ListView):
    model = Post
