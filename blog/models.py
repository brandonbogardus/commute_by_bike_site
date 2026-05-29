from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):               # Model for blog post.
    """Model for blog post"""
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):  # This method returns a string representation of the Post instance, which is the title of the post.
        return self.title

    def get_absolute_url(self):         # This method is used to get the URL for the detail view of the post.
        return reverse("blog:detail", kwargs={"pk": self.pk})

class PostImage(models.Model):          # Model for storing images associated with each blog post.
    """Model for post image. """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="post_images/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):   # This method returns a string representation of the PostImage instance, which includes the title of the associated post.
        return f"Image for: {self.post.title}"
