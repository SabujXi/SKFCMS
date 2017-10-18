from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View


def login_view(request):
	template='ecom_app/frontend/login.html'
	title='Login Page'
	context={'title':title}
	return render(request, template, context)