from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from decorators_module.my_custom_auth_decorators import custom_admin_decorator, custom_manager_decorator, custom_admin_manager_decorator


# Create your views here.
# @login_required(login_url='/login')

@custom_admin_manager_decorator
def back_index_view(request):
    template = 'ecom_app/backend/index.html'
    context = {'title': 'E-Commerce Admin Panel', 'heading': 'Dashboard'}
    return render(request, template, context)
