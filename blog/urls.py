from django.urls import path
from .views import BlogListView, BlogDetailView, BlogPostCreateView

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="index"),                     # blog index url
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),         # blog detail url
    path("new/", BlogPostCreateView.as_view(), name="create"),          # blog new post url
]
