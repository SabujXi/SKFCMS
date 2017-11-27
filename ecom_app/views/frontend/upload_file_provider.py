from django.http import FileResponse
from django.conf import settings
from django.http.response import HttpResponseNotFound
import os


# Create your views here.

def upload_file_provider_view(request, file_path=""):
    path = os.path.join(settings.UPLOAD_DIR, file_path)
    if os.path.exists(path) and os.path.isfile(path):
        return FileResponse(open(path, "rb"))
    else:
        return HttpResponseNotFound("NOoooooooOOOttttFound: %s" % file_path)
