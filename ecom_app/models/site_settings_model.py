from django.db import models


class SiteSetting(models.Model):
    title = models.CharField(max_length=100, default="")
    logo_file_path = models.CharField(max_length=300, default="")
    meta_title = models.CharField(max_length=200, default="")
    meta_description = models.TextField(default="")
    meta_keyword = models.CharField(max_length=200)
    short_desc = models.TextField(default="")
    long_desc = models.TextField(default="")
    phone = models.CharField(max_length=15, default="")
    email = models.CharField(max_length=100, default="")
    contact_details = models.TextField(default="")
    facebook_url = models.CharField(max_length=300, default="")
    twitter_url = models.CharField(max_length=300, default="")
    google_plus_url = models.CharField(max_length=300, default="")
    youtube_url = models.CharField(max_length=300, default="")
    copyrights = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    def get_logo_file_path(self):
        return self.logo_file_path
