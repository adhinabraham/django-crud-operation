from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=200)
    email=models.TextField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
         return "something"