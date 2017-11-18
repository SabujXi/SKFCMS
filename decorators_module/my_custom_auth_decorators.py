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
            if my_user.position == "ceo":
                messages.info(req, "Welcome CEO ")
                print("Welcome CEO ")
            else:  # req.user.users.position == "teacher":
                messages.warning(req, "You are not ceo! You can't access this page. ")
                logout(req)
                return redirect('ecom_app:login')
        return view_fun(req, *args, **kwargs)

    return view_fun_wrapper