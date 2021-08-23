from django.db import models
from django.contrib.auth.models import User

POST_CHOICES = (
    ("BLOG", "BLOG"),
    ("CODEGIST", "CODEGIST"),
)

LANGUAGE_CHOICES = (
    ("C" , "C"),
    ("PYTHON", "Python"),
    ("JAVA", "Java"),
    ("JAVASCRIPT", "Javascript"),
    ("CPP", "CPP"),
    ("OTHER", "other")
)

DIFFICULTIES = (
    ("DIFFICULT", "Difficult"),
    ("INTERMEDIATE", "Intermediate"),
    ("EASY", "Easy"),
)

# Create your models here.
class UserProfile(models.Model):
    user_ref = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    friends = models.ManyToManyField(User, related_name="user_friends")

class Category(models.Model):
    image = models.CharField(max_length=200)
    category_name = models.CharField(max_length=50, unique=True, default=None)
    description = models.CharField(max_length=200)

class Post(models.Model):
    post_type = models.CharField(choices=POST_CHOICES, max_length=10)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    post_ref = models.OneToOneField(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

class Blog(models.Model):
    post_ref = models.OneToOneField(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    content = models.CharField(max_length=2500, default=None)

class CodeGist(models.Model):
    post_ref = models.OneToOneField(Post, on_delete=models.CASCADE)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20,)
    analogy = models.CharField(max_length=1000, default="")
    code_snippet = models.CharField(max_length=1000, default="")
    topic = models.CharField(max_length=50, null=True)
    difficulty = models.CharField(choices=DIFFICULTIES, null=True, default="EASY", max_length=15)

