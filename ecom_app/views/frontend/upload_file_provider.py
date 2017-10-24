from django.http import FileResponse
from django.conf import settings
import os


# Create your views here.

def upload_file_provider_view(request, file_path=""):
    path = settings.UPLOAD_DIR + os.sep + file_path
    return FileResponse(open(path, "rb"))
