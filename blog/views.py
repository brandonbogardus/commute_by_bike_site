from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import PostForm
from .models import Post


class BlogListView(ListView):
    model = Post
    ordering = ["-date_posted"]
    paginate_by = 5
    template_name = "blog/index.html"


class BlogDetailView(DetailView):
    model = Post


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  # set author before saving
        return super().form_valid(form)
