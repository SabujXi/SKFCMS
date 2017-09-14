from django.db import models

class Brands(models.Model):
	name = models.CharField(max_length = 120, default = "")
	slug = models.CharField(max_length = 120, unique = True)
	description = models.TextField(default = "")