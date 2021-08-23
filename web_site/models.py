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

CODING_PLATFORMS = (
    ("HACKERRANK", "HackerRank"),
    ("CODECHEF", "CodeChef"),
    ("LEETCODE", "Leetcode"),
    ("NONE", "None"),
)

DIFFICULTIES = (
    ("DIFFICULT", "Difficult"),
    ("INTERMEDIATE", "Intermediate"),
    ("EASY", "Easy"),
)

# Create your models here.
class UserProfile(models.Model):
    user_ref = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    image = models.CharField(max_length=200)
    category_name = models.CharField(max_length=50, unique=True, default=None)
    description = models.CharField(max_length=200)

class Post(models.Model):
    post_type = models.CharField(choices=POST_CHOICES, max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True, default=None)

class Blog(models.Model):
    post_ref = models.OneToOneField(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    content = models.CharField(max_length=250, default=None)

class CodeGist(models.Model):
    post_ref = models.OneToOneField(Post, on_delete=models.CASCADE)
    coding_platform = models.CharField(choices=CODING_PLATFORMS, max_length=30)
    problem_url = models.URLField(default="", null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20,)
    analogy = models.CharField(max_length=250, default="")
    code_snippet = models.CharField(max_length=250, default="")
    topic = models.CharField(max_length=50, null=True)
    difficulty = models.CharField(choices=DIFFICULTIES, null=True, default="EASY", max_length=15)

