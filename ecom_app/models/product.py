from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120, default="")
    description = models.TextField(default="")
    shortdescription = models.TextField(default="")
    price = models.FloatField()
    discount = models.FloatField()
    stock_status = models.CharField(max_length=64)
    sku = models.CharField(max_length=64)
    category = models.ManyToManyField("ecom_app.Category")
    tags = None
    imageurl = models.CharField(max_length=32, default="")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


