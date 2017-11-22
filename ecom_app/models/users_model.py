from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model


class Users(models.Model):
    dj_user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, default="")
    position = models.CharField(max_length=24, default="user")

    reset_password_token = models.CharField(max_length=128, null=True, default=None, unique=True)
    reg_complete_token = models.CharField(max_length=128, null=True, default=None, unique=True)

    @property
    def is_user(self):
        if self.position == "user":
            return True
        return False

    @property
    def is_manager(self):
        if self.position == "manager":
            return True
        return False
