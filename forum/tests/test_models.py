from django.test import TestCase
from django.contrib.auth import get_user_model
from forum.models import Thread, Comment

User = get_user_model()


class ForumModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )
        cls.thread = Thread.objects.create(
            title="Test Thread",
            content="Some content.",
            author=cls.user,
        )

    def test_str_method(self):
        self.assertEqual(self.thread.__str__(), "Test Thread")

    def test_get_absolute_url(self):
        self.assertEqual(self.thread.get_absolute_url(), f"/forum/{self.thread.pk}/")

class ForumCommentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )
        cls.thread = Thread.objects.create(
            title="Test Thread",
            content="Some content.",
            author=cls.user,
        )
        cls.comment = Comment.objects.create(
            content="This is a test comment.",
            author=cls.user,
            thread=cls.thread
        )

    def test_str_method(self):
        self.assertEqual(self.comment.__str__(), "This is a test comment.")
