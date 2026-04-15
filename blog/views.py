from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import PostForm, PostImageFormSet
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
        form.instance.author = self.request.user  # 1. Assign the logged-in user as author
        self.object = form.save()                 # 2. Save the Post first (formset needs its PK)
        formset = PostImageFormSet(               # 3. Bind the formset to the saved Post
            self.request.POST,
            self.request.FILES,
            instance=self.object
        )
        if formset.is_valid():
            formset.save()                                  # 4. Save the images
        return redirect(self.object.get_absolute_url())     # 5. Redirect manually

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       # 1. Get everything the default provides
        context["image_formset"] = PostImageFormSet()      # 2. Add a blank formset on top of it
        return context