from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    dj_user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, default="")
    position = models.CharField(max_length=24, default="ceo", choices=[('teacher', 'teacher'), ('ceo', 'ceo')])