from django.test import TestCase
from django.contrib.auth import get_user_model
from forum.models import Thread, Comment

User = get_user_model()

class ForumListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )
        cls.thread = Thread.objects.create(
            title="Test Thread.",
            content="Some content.",
            author=cls.user,
        )

    def test_forum_list_view(self):
        response = self.client.get("/forum/")
        self.assertEqual(response.status_code, 200)

    def test_forum_list_view_template(self):
        response = self.client.get("/forum/")
        self.assertTemplateUsed(response, "forum/thread_list.html")

    def test_forum_list_view_contains_thread(self):
        response = self.client.get("/forum/")
        self.assertIn(self.thread, response.context["object_list"])