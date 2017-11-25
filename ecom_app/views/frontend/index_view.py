from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View


# Create your views here.

def front_index_view(request):

    # if not request.user.is_anonymous:
    #     if request.user.is_stuff:
    #         pass
    #     elif request.user.is_superuser:
    #         pass
    #     else:
    #         pass
    #         # normal user
    #         # not stuff and not superuser
    # else:
    #     pass

    template = 'ecom_app/frontend/index.html'
    title = 'Home Page'
    products = models.Product.objects.all()
    context = {'products': products, 'title': title}
    return render(request, template, context)
