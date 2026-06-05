from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from .forms import ThreadForm, CommentForm
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
    template_name = "forum/thread_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user    # set the logged-in user as the form author
        self.object = form.save()           
        return redirect(self.object.get_absolute_url())
    
class ForumThreadDeleteView(LoginRequiredMixin, DeleteView):
    model = Thread
    success_url = reverse_lazy("forum:index")

class ForumAddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "forum/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        thread = Thread.objects.get(pk=self.kwargs["pk"])
        form.instance.thread = thread
        self.object = form.save()
        return redirect(thread.get_absolute_url())
        

class ForumDeleteCommentView(LoginRequiredMixin, DeleteView):