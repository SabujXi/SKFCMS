from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View
from django.contrib.auth.decorators import login_required
from decorators_module.my_custom_auth_decorators import my_custom_position_decorator


# Create your views here.
# @login_required(login_url='/login')
@my_custom_position_decorator
def back_index_view(request):
    template = 'ecom_app/backend/index.html'
    context = {'title': 'E-Commerce Admin Panel', 'heading': 'Dashboard'}
    return render(request, template, context)
