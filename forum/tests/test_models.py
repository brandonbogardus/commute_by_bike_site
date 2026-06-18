from django.test import TestCase
from django.contrib.auth import get_user_model
from forum.models import Thread, Comment

User = get_user_model()


class ForumModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_superuser(
            username="testuser",
            password="password123",
        )
        cls.thread = Thread.objects.create(
            title="Test Thread",
            content="Some content.",
            author=cls.user,
        )
