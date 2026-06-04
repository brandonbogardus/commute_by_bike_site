from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import ThreadForm
from .models import Thread, Comment


class ForumListView(ListView):
    model = Thread
    ordering = ["-date_posted"]
    paginate_by = 10


class ForumThreadView(DetailView):
    model = Thread

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # get the Thread context data
        context["comments"] = self.object.comments.all() # add comments via "related_name" in Thread foreighkey on Comment model
        return context
    
class ForumThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = "form/thread_form.html"

    