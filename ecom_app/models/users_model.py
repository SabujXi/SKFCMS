from django.db import models


class Users(models.Model):
    user_name = models.CharField(max_length=120, unique=True)
    email = models.CharField(max_length=120, unique=True)
    password = models.CharField(max_length=12, null=True)