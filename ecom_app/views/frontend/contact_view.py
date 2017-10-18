from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View


def contact_view(request):
	template='ecom_app/frontend/contact.html'
	title='Contact Page'
	context={'title':title}
	return render(request, template, context)