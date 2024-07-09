from django.db import models

# Create your models here.
class NPC(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

