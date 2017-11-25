from django.shortcuts import render
from ecom_app.models import SiteSetting
from django.views import View
from django.http import FileResponse
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from decorators_module.my_custom_auth_decorators import custom_admin_decorator


# Create your views here.
@method_decorator(custom_admin_decorator, name="dispatch")
class CrudSiteSetting(View):
    template = "ecom_app/backend/site_settings.html"
    # How to apply this decorator on class

    def get(self, request, site_id=None):
        if site_id:
            site = SiteSetting.objects.get(pk=site_id)
            context = {'title': 'Site Settings', 'site': site, 'heading': 'Site Settings'}
            return render(request, self.template, context)
        else:
            return render(request, self.template, {'title': 'Site Settings','heading': 'Site Settings'})

    def post(self, request, site_id=None):
        title = request.POST.get('site_title', '')
        logo_file = request.FILES.get('image_file', None)

        if logo_file is not None:
            logo_file_path = logo_file.name
        else:
            logo_file_path = ""

        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_desc', '')
        meta_keyword = request.POST.get('meta_keyword', '')
        short_desc = request.POST.get('short_desc', '')
        long_desc = request.POST.get('long_desc', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        contact_details = request.POST.get('contact_details', '')
        facebook_url = request.POST.get('facebook', '')
        twitter_url = request.POST.get('twitter', '')
        google_plus_url = request.POST.get('google_plus', '')
        youtube_url = request.POST.get('youtube', '')
        copyrights = request.POST.get('copyright', '')
        # create_date = None
        # update_date = None

        if site_id:
            site = SiteSetting.objects.get(pk=site_id)
            site.title = title
            site.logo_file_path = logo_file_path
            site.meta_title = meta_title
            site.meta_description = meta_description
            site.meta_keyword = meta_keyword
            site.short_desc = short_desc
            site.long_desc = long_desc
            site.phone = phone
            site.email = email
            site.contact_details = contact_details
            site.facebook_url = facebook_url
            site.twitter_url = twitter_url
            site.google_plus_url = google_plus_url
            site.youtube_url = youtube_url
            site.copyrights = copyrights
            # loc.active=status
            site.save()
            msg = 'Data Updated Successfully'
        else:
            site = SiteSetting(
                title=title,
                logo_file_path=logo_file_path,
                meta_title=meta_title,
                meta_description=meta_description,
                meta_keyword=meta_keyword,
                short_desc=short_desc,
                long_desc=long_desc,
                phone = phone,
                email = email,
                contact_details = contact_details,
                facebook_url = facebook_url,
                twitter_url = twitter_url,
                google_plus_url = google_plus_url,
                youtube_url = youtube_url,
                copyrights=copyrights
            )
            site.save()

            if logo_file:
                with open(settings.UPLOAD_DIR + os.sep + logo_file.name, "wb") as fw:
                    for c in logo_file.chunks():
                        fw.write(c)

            msg = 'Data Inserted Successfully'
        context = {'title': 'Site Settings Form','heading': 'Site Settings', 'site': site, 'msg': msg}
        return render(request, self.template, context)
