from django.shortcuts import render, redirect
from ecom_app import models
from django.views import View

class CrudUser(View):
    template = 'ecom_app/backend/user_form.html'
    heading = 'User Form'

    def get(self, req, user_id=None):
        if user_id:
            user_id = int(user_id)
            users = models.Users.objects.get(id=user_id)
            return render(req, self.template, context={
                'user': users, 'heading':self.heading
            })
        else:
            return render(req, self.template, context={
                'heading':self.heading
            })

    def post(self, req, user_id=None):

        name = req.POST['name']
        email = req.POST['email']
        password = req.POST['password']

        if user_id:
            user_id = int(user_id)
            user = models.Users.objects.get(id=user_id)
            user.user_name = name
            user.email = email
            user.password = password
            user.save()
            msg = "Record Updated [" + "User id: " + str(user.id) +  "]"
        else:
            user = models.Users(
                user_name = name,
                email = email,
                password = password
            )
            user.save()
            msg = "Successfully saved [" + "User id: " + str(user.id) + "]"

        return render(req, self.template, context={
            'msg': msg,
            'user': user,
            'heading':self.heading
        })


def UserListView(req):
    users = models.Users.objects.all()
    return render(req, 'ecom_app/backend/user_list.html', context={
        'users': users,
        'heading': 'Customer List'
    })


'''
def BrandsDeleteView(req, brands_id):
    brands_id = int(brands_id)
    brand = models.Brands.objects.get(id=brands_id)
    brand.delete()
    return redirect("ecom_app:brands_list")
'''