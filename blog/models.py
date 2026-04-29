from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    """Model for blog post"""
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})     #returns the blog detail page

class PostImage(models.Model):
    """Model for post image. """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="post_images/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for: {self.post.title}"
