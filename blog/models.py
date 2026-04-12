from django.conf import settings
from django.db import models
from django.urls import reverse

class Post(models.Model):
    """Model for blog post"""
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    autthor = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})