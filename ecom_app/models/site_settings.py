from django.db import models


class SiteSetting(models.Model):
    title = models.CharField(max_length=100)
    logo_file_path = models.CharField(max_length=300, default="")
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    meta_keyword = models.CharField(max_length=200)
    short_desc = models.TextField()
    long_desc = models.TextField()
    copyrights = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    def get_logo_file_path(self):
        return self.logo_file_path
