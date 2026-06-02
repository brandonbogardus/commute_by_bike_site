from django.db import models
from django.conf import settings
from django.urls import reverse


class Thread(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("forum:thread", kwargs={"pk": self.pk})


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
    )
    date_posted = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(
        Thread, on_delete=models.CASCADE, related_name="comments"
    )
    quote = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.content[:50]
