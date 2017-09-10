from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View

# Create your views here.

def front_index_view(request):
	template='ecom_app/frontend/index.html'
	context={'title':'Welcome'}
	return render(request, template, context)

def back_index_view(request):
	template='ecom_app/backend/index.html'
	context={'title':'Ecom Admin Panel'}
	return render(request, template, context)


def product_menu_view(request):
	template='ecom_app/backend/prod_menu.html'
	context={'title':'Product Menu'}
	return render(request, template, context)


def category_menu_view(request):
	template='ecom_app/backend/cat_menu.html'
	context={'title':'Category Menu'}
	return render(request, template, context)