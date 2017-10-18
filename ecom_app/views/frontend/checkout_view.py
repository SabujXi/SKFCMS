from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View




def checkout_view(request):
	template='ecom_app/frontend/checkout.html'
	title='Checkout Page'
	context={'title':title}
	return render(request, template, context)