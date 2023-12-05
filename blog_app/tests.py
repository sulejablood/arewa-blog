from django.test import TestCase
from .models import Post

# Create your tests here.
class PostModelTest (TestCase):
    def test_string_representation(self):
        post = Post(title="Test Post")
        self.assertEqual(str(post), "Test Post")