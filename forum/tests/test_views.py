from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
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
        response = self.client.get(reverse("forum:index"))
        self.assertEqual(response.status_code, 200)

    def test_forum_list_view_template(self):
        response = self.client.get(reverse("forum:index"))
        self.assertTemplateUsed(response, "forum/thread_list.html")

    def test_forum_list_view_contains_thread(self):
        response = self.client.get(reverse("forum:index"))
        self.assertIn(self.thread, response.context["object_list"])


class ForumDetailViewTests(TestCase):
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

        cls.comment = Comment.objects.create(
            content="Test comment.",
            author=cls.user,
            thread=cls.thread,
        )

    def test_forum_detail_view(self):
        response = self.client.get(
            reverse("forum:thread", kwargs={"pk": self.thread.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_forum_detail_view_template(self):
        response = self.client.get(
            reverse("forum:thread", kwargs={"pk": self.thread.pk})
        )
        self.assertTemplateUsed(response, "forum/thread_detail.html")

    def test_forum_detail_view_contains_comment(self):
        response = self.client.get(
            reverse("forum:thread", kwargs={"pk": self.thread.pk})
        )
        self.assertIn(self.comment, response.context["comments"])

    def test_forum_detail_view_nonexistent(self):
        response = self.client.get(
            reverse("forum:thread", kwargs={"pk": self.thread.pk + 1})
        )
        self.assertEqual(response.status_code, 404)


# TODO use reverse to remove hard-coded urls below


class ForumThreadCreateViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )

    def test_forum_thread_create_view_with_loggedin_user(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get("/forum/new/")
        self.assertEqual(response.status_code, 200)

    def test_forum_thread_create_view_redirect_for_unauthorized(self):
        response = self.client.get("/forum/new/")
        self.assertEqual(response.status_code, 302)

    def test_forum_thread_create_view_redirects_to_detail_for_authorized(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(
            "/forum/new/", data={"title": "New Thread", "content": "New Content"}
        )
        thread = Thread.objects.get(title="New Thread")
        self.assertRedirects(response, f"/forum/{thread.pk}/")

    def test_forum_thread_create_view_new_thread_exists(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(
            "/forum/new/", data={"title": "New Thread", "content": "New Content"}
        )
        self.assertTrue(Thread.objects.filter(title="New Thread").exists())
