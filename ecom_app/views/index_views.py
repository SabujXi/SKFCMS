from django.shortcuts import render
from ecom_app import models

# Create your views here.
def index_view(req):
    return render(req, 'ecom_app/index.html')

