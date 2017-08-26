from django.shortcuts import render
from ecom_app import models

# Create your views here.
def index_view(req):
    return render(req,'ecom_app/index.html')

def categoryform_view(req):
    return render(req, 'ecom_app/category_form.html')


def categorylist_view(req):
    cats = models.Category.objects.all()
    return render(req, 'ecom_app/category_list.html', context={
        'cats': cats
    })
