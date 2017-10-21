from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View

from django.shortcuts import render, redirect
from ecom_app import models
from django.views import View


class UserReg(View):
    template = 'ecom_app/frontend/login.html'
    title = 'Login Form'
    heading = 'Login Form'

    def get(self, req, user_id=None):
        if user_id:
            user_id = int(user_id)
            users = models.Users.objects.get(id=user_id)
            context = {'users': users, 'heading': self.heading, 'title':self.title}
            return render(req, self.template, context)
        else:
            context = {'heading': self.heading, 'title':self.title}
            return render(req, self.template, context)

    def post(self, req, user_id=None):
        user_name = req.POST['user_name']
        email = req.POST['email']
        password = req.POST['password']

        if user_id:
            user_id = int(user_id)
            user = models.Users.objects.get(id=user_id)
            user.user_name = user_name
            user.email = email
            user.password = password
            user.save()
            msg = "Record Updated"

        else:
            user= models.Users(
                user_name = user_name,
                email = email,
                password = password
            )
            user.save()
            msg = "Successfully saved"

        return render(req, self.template, context={'msg': msg, 'user':user, 'heading':self.heading, 'title':self.title})
