from django.db import models
from django.conf import settings
from django.urls import reverse


class Thread(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
    )
