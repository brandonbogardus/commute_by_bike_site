from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("blog:index")


    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

