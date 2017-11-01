from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    short_description = models.TextField()
    category = models.ManyToManyField("ecom_app.Category")
    tags = models.ManyToManyField("ecom_app.Tags")
    price = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    stock_status = models.CharField(max_length=1, null=True)
    image_file_path = models.CharField(max_length=300, default="")
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    brands = models.ForeignKey("Brands", on_delete=models.CASCADE, blank=True, null=True)

    def get_image_file_path(self):
        return self.image_file_path

