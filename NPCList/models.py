from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class NPC(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    genre = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="NPC_posts"
)


def __str__(self):
        return self.title

