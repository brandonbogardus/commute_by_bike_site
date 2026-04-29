from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post, PostImage
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class PostModelTests(TestCase):
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

    def test_str_method(self):
        self.assertEqual(self.post.__str__(), "Test Post")

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), f"/{self.post.pk}/")


class PostImageModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser2", password="password123"
        )
        cls.post = Post.objects.create(
            title="Test Post 2", content="Some content.", author=cls.user
        )
        fake_image = SimpleUploadedFile(
            "test.jpg", b"file_content", content_type="image/jpeg"
        )
        cls.post_image = PostImage.objects.create(
            post=cls.post,
            image=fake_image,
            caption="A test caption",
        )

    def test_str_method(self):
        self.assertEqual(self.post_image.__str__(), "Image for: Test Post 2")
