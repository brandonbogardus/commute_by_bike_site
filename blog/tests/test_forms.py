from django.test import TestCase
from blog.forms import PostForm


class PostFormTests(TestCase):

    def test_form_accepts_valid_data(self):
        form = PostForm(data={"title": "Post Title", "content": "Some content."})
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
