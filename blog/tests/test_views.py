from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post

User = get_user_model()


class BlogListViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )

        cls.post = Post.objects.create(
            title="Test Post",
            content="Some content.",
            author=cls.user,
        )

    def test_blog_list_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_blog_list_view_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_blog_list_view_contains_post(self):
        response = self.client.get("/")
        self.assertIn(self.post, response.context["object_list"])


class BlogDetailViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )

        cls.post = Post.objects.create(
            title="Test Post",
            content="Some content.",
            author=cls.user,
        )

    def test_blog_detail_view(self):
        response = self.client.get(f"/{self.post.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_view_template(self):
        response = self.client.get(f"/{self.post.pk}/")
        self.assertTemplateUsed(response, "blog/post_detail.html")


class BlogPostCreateViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )


    def test_blog_create_view_with_loggedin_user(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get("/new/")
        self.assertEqual(response.status_code, 200)


    def test_blog_create_view_redirect_for_unauthorized(self):
        response = self.client.get("/new/")
        self.assertEqual(response.status_code, 302)


    def test_blog_create_view_new_post(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post("/new/", data={"title": "New Post", "content": "New Content"})
        self.assertTrue(Post.objects.filter(title="New Post").exists())
