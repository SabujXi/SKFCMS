from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    short_description = models.TextField()
    category = models.ManyToManyField("ecom_app.Category")
    tags = models.ManyToManyField("ecom_app.Tags")
    price = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    stock_status = (
				        ('A', 'Available'),
				        ('U', 'Unavailable'),
		          )
    imageurl = models.CharField(max_length=300, default="")
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)