from django.db import models 

Class NPC(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)
    #role
    user = models.ForeignKey
