from django.db import models
from .choices.choices import menu_type_choices


class MenuModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(default = "")
    parent = models.ForeignKey("self",null=True)
    type = models.CharField(max_length=64,choices=menu_type_choices)
    content = models.TextField(default="")
    serial_no = models.IntegerField(default=0)
    disabled = models.BooleanField()

    def __str__(self):
        return self.name
