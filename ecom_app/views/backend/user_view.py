from django.shortcuts import render, redirect
from ecom_app import models
from django.views import View
from django.contrib.auth.models import User as Djuser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ecom_app.models.choices.choices import position_choices
from django.utils.decorators import method_decorator
from decorators_module.my_custom_auth_decorators import custom_admin_decorator, custom_manager_decorator, custom_admin_manager_decorator


class BackendUserLogin(View):

    template = 'ecom_app/backend/login_form.html'

    def get(self, req):
        return render(req, self.template, {})

    def post(self, req):
        username = req.POST['username']
        password = req.POST['password']
        # print(username)
        back_user = authenticate(req, username=username, password=password)
        if back_user:
            login(req, back_user)
            return redirect('ecom_app:back-index')
        else:
            messages.info(req, "Invalid Credentials")
            return redirect('ecom_app:user-login')


@custom_admin_manager_decorator
def backend_logout_view(request):
    logout(request)
    return redirect('ecom_app:user-login')


@custom_admin_decorator
def user_list_view(req):
    template = 'ecom_app/backend/user_list.html'
    users = models.Users.objects.all()
    context = { 'users': users, 'heading': 'User List' }
    return render(req, template, context)


@method_decorator(custom_admin_decorator, name="dispatch")
class CrudUser(View):
    template = 'ecom_app/backend/user_form.html'
    heading = 'User Form'

    def get(self, req, user_id=None):
        if user_id:
            user_id=int(user_id)
            user = models.Users.objects.get(dj_user_id=user_id)
            context = {'position':position_choices, 'user':user, 'heading': 'Update User'}
        else:
            context = {'heading': 'Create User', 'position':position_choices,}

        return render(req, self.template, context)

    def post(self, req, user_id=None):
        name = req.POST['name']
        mobile = req.POST['mobile']
        # email = req.POST['email']
        # username = req.POST['username']
        password = req.POST['password']
        user_position = req.POST['position']

        if user_id:
            user_id=int(user_id)
            duser = Djuser.objects.get(pk=user_id)
            duser.first_name=name
            duser.set_password(password)
            duser.save()

            user = models.Users.objects.get(dj_user_id=user_id)
            user.mobile=mobile
            user.position=user_position
            user.save()

        return redirect('ecom_app:user-form', user.dj_user_id)



'''
def BrandsDeleteView(req, brands_id):
    brands_id = int(brands_id)
    brand = models.Brands.objects.get(id=brands_id)
    brand.delete()
    return redirect("ecom_app:brands_list")
'''