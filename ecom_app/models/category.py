from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=150, default="")
    slug=models.CharField(max_length=150, unique=True)
    description=models.TextField(default="")
