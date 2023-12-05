# create_post.py

from blog_app.models import Post
from django.utils import timezone

# Create a new post instance
new_post = Post(title='My First Post', content='This is the content of the post.', pub_date=timezone.now())
new_post.save()
