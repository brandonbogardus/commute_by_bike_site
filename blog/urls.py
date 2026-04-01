from django.urls import path
from .views import BlogListView

app_name = "blog"

url_patterns = [
    # blog index
    path("", BlogListView.as_view(), name="index")
]

