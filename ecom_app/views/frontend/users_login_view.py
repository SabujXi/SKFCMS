



from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from ecom_app import models
from django.views import View
from django.contrib.auth.models import User as DjUser
from django.contrib.auth import authenticate, login


class UserReg(View):
    template = 'ecom_app/frontend/login.html'
    title = 'Login Form'
    heading = 'Login Form'

    def get(self, req):
        context = {'heading': self.heading, 'title': self.title}
        return render(req, self.template, context)

    def post(self, req):
        user_name = req.POST['user_name']
        email = req.POST['email']
        password = req.POST['password']
        djuser = DjUser.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        djuser.first_name=user_name
        djuser.save()

        # Relation
        user = models.Users(
            dj_user=djuser
        )
        user.save()
        messages.info(req,"Successfully saved - Please Login!")

        return redirect('ecom_app:login')


class UserLogin(UserReg):

    def post(self, req):
        email = req.POST['email']
        password = req.POST['password']
        djuser = authenticate(req, username=email, password=password)
        if djuser:
            login(req, djuser)
            messages.info(req, "Logged in success")
        else:
            messages.info(req, "Invalid Credentials")

        return redirect('ecom_app:login')
