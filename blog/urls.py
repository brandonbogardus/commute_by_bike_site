from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = "blog"

urlpatterns = [
    # blog index
    path("", BlogListView.as_view(), name="index"),
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
]

