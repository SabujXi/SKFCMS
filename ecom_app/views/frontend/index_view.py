from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View


# Create your views here.

def front_index_view(request):
    template = 'ecom_app/frontend/index.html'
    title = 'Home Page'
    products = models.Product.objects.all()
    context = {'products': products, 'title': title}
    return render(request, template, context)
