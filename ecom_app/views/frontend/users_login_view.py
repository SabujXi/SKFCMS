from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from ecom_app import models
from django.views import View
from django.contrib.auth.models import User as DjUser
from django.contrib.auth import authenticate, login, logout


class UserReg(View):
    template = 'ecom_app/frontend/login.html'
    title = 'Login Form'
    heading = 'Login Form'

    def get(self, req):
        context = {'heading': self.heading, 'title': self.title}
        return render(req, self.template, context)

    def post(self, req):
        name = req.POST['name']
        mobile = req.POST['mobile']
        email = req.POST['email']
        username = req.POST['username']
        password = req.POST['password']
        djuser = DjUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        djuser.first_name=name
        djuser.save()

        # Relation
        user = models.Users(
            dj_user=djuser,
            mobile = mobile
        )
        user.save()
        messages.info(req,"Successfully saved - Please Login!")

        return redirect('ecom_app:login')


class UserLogin(UserReg):

    def post(self, req):
        username = req.POST['username']
        password = req.POST['password']
        djuser = authenticate(req, username=username, password=password)
        if djuser:
            login(req, djuser)
            return redirect('ecom_app:front-index')
        else:
            messages.info(req, "Invalid Credentials")
            return redirect('ecom_app:login')

def logout_view(request):
    logout(request)
    return redirect('ecom_app:login')