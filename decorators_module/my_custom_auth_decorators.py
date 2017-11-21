from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from ecom_app.models.users_model import Users


def my_custom_position_decorator(view_fun):
    def view_fun_wrapper(req, *args, **kwargs):
        # if req.user.is_anonymous:
        #     return redirect("/login")
        # else:
        #     # so, u r logged in
        #     if req.user.is_stuff and req.user.is_superuser:
        #         pass
        #     elif req.user.is_stuff:
        #         pass
        #     elif req.user.is_superuser:
        #         pass
        #     else:
        #         pass
        # custom way
        if req.user.is_anonymous:
            return redirect("/login")
        else:
            my_user = Users.objects.get(dj_user=req.user)
            if my_user.position == "admin":
                pass
            else:  # req.user.users.position == "teacher":
                # messages.warning(req, "You are not Admin! You can't access this page. ")
                logout(req)
                return redirect('ecom_app:login')
        return view_fun(req, *args, **kwargs)

    return view_fun_wrapper


# Custom Admin Decorator
def custom_admin_decorator(view_fun):
    def view_fun_wrapper(req, *args, **kwargs):
        if req.user.is_anonymous:
            messages.warning(req, "Request not valid! ")
            return redirect('ecom_app:login')
        else:
            my_user = Users.objects.get(dj_user=req.user)
            if my_user.position == "user":
                messages.warning(req, "Request not valid! ")
                return redirect('ecom_app:login')
            elif my_user.position == "admin":
                pass
            else:
                messages.warning(req, "You are not Admin! You can't access this page. ")
                # logout(req)
                return redirect('ecom_app:back-index')
        return view_fun(req, *args, **kwargs)

    return view_fun_wrapper


# Custom Manager Decorator
def custom_manager_decorator(view_fun):
    def view_fun_wrapper(req, *args, **kwargs):
        if req.user.is_anonymous:
            messages.warning(req, "Request not valid! ")
            return redirect('ecom_app:login')
        else:
            my_user = Users.objects.get(dj_user=req.user)
            if my_user.position == "user":
                messages.warning(req, "Request not valid! ")
                return redirect('ecom_app:login')
            elif my_user.position == "manager":
                pass
            else:
                messages.warning(req, "You are not Manager! You can't access this page. ")
                # logout(req)
                return redirect('ecom_app:back-index')
        return view_fun(req, *args, **kwargs)

    return view_fun_wrapper


def custom_admin_manager_decorator(view_fun):
    def view_fun_wrapper(req, *args, **kwargs):
        if req.user.is_anonymous:
            messages.warning(req, "Request not valid! ")
            return redirect('ecom_app:login')
        else:
            my_user = Users.objects.get(dj_user=req.user)
            if my_user.position == "user":
                messages.warning(req, "Request not valid! ")
                return redirect('ecom_app:login')
            elif my_user.position == "admin" or my_user.position == "manager":
                pass
            else:
                messages.warning(req, "You are not Admin or Manager! You can't access this page. ")
                # logout(req)
                return redirect('ecom_app:back-index')
        return view_fun(req, *args, **kwargs)

    return view_fun_wrapper