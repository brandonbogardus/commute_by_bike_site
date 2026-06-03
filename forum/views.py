from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Thread, Comment


class ForumListView(ListView):
    model = Thread
    ordering = ["-date_posted"]
    paginate_by = 10


class ForumThreadView(DetailView):
    model = Thread

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
