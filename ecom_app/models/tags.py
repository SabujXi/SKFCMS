from django.db import models

class Tags(models.Model):
    name=models.CharField(max_length=150, default="")
    slug=models.CharField(max_length=150, unique=True)
    description=models.TextField(default="")

    def __str__(self):              # __unicode__ on Python 2
        return self.name