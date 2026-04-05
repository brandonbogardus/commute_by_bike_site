from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    ordering = ["-date_posted"]
    paginate_by = 5
    template_name = "blog/index.html"


class BlogDetailView(DetailView):
    model = Post
