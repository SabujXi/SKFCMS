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
from django.core.mail import send_mail
from uuid import uuid4
from django.urls import reverse_lazy
from django.urls import reverse

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
        djuser.first_name = name
        djuser.is_active = False

        # Relation
        user = models.Users(
            dj_user=djuser,
            mobile = mobile,
            is_reset_req_flag = False
        )
        token = username + uuid4().hex
        abs_url = req.build_absolute_uri(reverse("ecom_app:email-verification", kwargs={"token":token}))
        user.reg_complete_token = token
        # djuser.save()
        # user.save()
        # messages.info(req,"Successfully saved - Please Login!")
        res = send_mail("Registration complete", "You have completed your registration,"
                                                  "please click the following link to confirm your email: %s" % abs_url, "firoz@medisys.com", [email])

        if res == 1:
            djuser.save()
            user.save()

        messages.info(req, "Please check your inbox to verify your email")

        return redirect('ecom_app:login')


def verify_email_view(req, token=None):
    try:
        user = models.Users.objects.get(reg_complete_token=token)
    except models.Users.DoesNotExist:
        user = None

    if user:
        user.dj_user.is_active = True
        user.dj_user.save()
        messages.info(req, "Verification successful! You may login now...")
    else:
        messages.warning(req, "Invalid token")
    return redirect("ecom_app:login")


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


def forgot_pass(request):
    template='ecom_app/frontend/forgot_pass.html'
    title = 'Forgot Password?'
    heading = 'Forgot Password?'

    if request.method == 'GET':
        context = {'heading': heading, 'title': title}
        return render(request, template, context)

    elif request.method == 'POST':
        email = request.POST['email']
        if email:
            try:
                dj_user = DjUser.objects.get(email=email)
            except DjUser.DoesNotExist:
                dj_user = None

        if dj_user:
            try:
                user = models.Users.objects.get(dj_user_id=dj_user.id)
            except models.Users.DoesNotExist:
                user = None

            if user:
                username = user.dj_user.username
                token = username + uuid4().hex
                abs_url = request.build_absolute_uri(reverse("ecom_app:reset-pass", kwargs={"token":token}))
                user.reset_password_token = token
                user.is_reset_req_flag = True
                res = send_mail("Reset Password", "Link : " "Please click the following link to reset password: %s" % abs_url, "firoz@medisys.com", [email])
                if res == 1:
                    user.save()
                    messages.info(request, "Please check your inbox!")

        return redirect('ecom_app:forgot-pass')


def reset_pass(request, token=None):
    template = 'ecom_app/frontend/reset_pass.html'
    title = 'Reset Password?'
    heading = 'Reset Password?'
    if request.method == 'GET':
        try:
            user = models.Users.objects.get(reset_password_token=token)
        except models.Users.DoesNotExist:
            user = None
        context = {'heading': heading, 'title': title, 'token':token, 'user_token':user}
        if user.is_reset_req_flag==True:
            return render(request, template, context)
        else:
            return render(request, 'ecom_app/frontend/404_page.html', {'title':'404 Page Not Found'})

    elif request.method == 'POST':
        token = request.POST.get('reset_token','')
        password = request.POST.get('reset_pass','')

        try:
            user = models.Users.objects.get(reset_password_token=token)
        except models.Users.DoesNotExist:
            user = None

        if user:
            if password:
                user.dj_user.set_password(password)
                user.is_reset_req_flag = False
                user.dj_user.save()
                user.save()
                messages.info(request, 'Password Reset Successful!')
        else:
            messages.info(request, 'Sorry, User not found!')


        return redirect('ecom_app:login')