from django.shortcuts import render, redirect
from ecom_app import models
from django.http import HttpResponse
from django.views import View

def category_form_view(req):
    if req.method == 'POST':
        name = req.POST['name']
        slug = req.POST['slug']
        desc = req.POST['desc']

        cat = models.Category(
            name=name,
            slug=slug,
            description=desc
        )
        cat.save()
        return HttpResponse("Data Saved")
    else:
        return render(req, 'ecom_app/category_form.html')


class CategoryCreateOrEditView(View):
    template = 'ecom_app/category_form.html'

    def get(self, req, cat_id=None):
        if cat_id:
            cat_id = int(cat_id)
            cat = models.Category.objects.get(id=cat_id)
            return render(req, self.template, context={
                'cat': cat
            })
        else:
            return render(req, self.template)

    def post(self, req, cat_id=None):

        name = req.POST['name']
        slug = req.POST['slug']
        desc = req.POST['desc']

        if cat_id:
            cat_id = int(cat_id)
            cat = models.Category.objects.get(id=cat_id)
            cat.name = name
            cat.slug = slug
            cat.description = desc
            cat.save()
            msg = "Record Updated [" + "Category id: " + str(cat.id) +  "]"
        else:
            cat = models.Category(
                name=name,
                slug=slug,
                description=desc
            )
            cat.save()
            msg = "Successfully saved [" + "Category id: " + str(cat.id) + "]"

        return render(req, self.template, context={
            'msg': msg,
            'cat': cat
        })

def category_list_view(req):
    cats = models.Category.objects.all()
    return render(req, 'ecom_app/category_list.html', context={
        'cats': cats
    })

def category_view_view(req, cat_id):
    template = "ecom_app/category_view.html"
    cat_id = int(cat_id)
    cat = models.Category.objects.get(id=cat_id)
    return render(req, template, context={
        'cat': cat
    })

def category_delete_view(req, cat_id):
    cat_id = int(cat_id)
    cat = models.Category.objects.get(id=cat_id)
    cat.delete()
    return redirect("ecom_app:cat_list")