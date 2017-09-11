from django.shortcuts import render, redirect
from ecom_app import models
from django.views import View

class BrandsCreateOrEditView(View):
    template = 'ecom_app/brands_form.html'

    def get(self, req, brands_id=None):
        if brands_id:
            brands_id = int(brands_id)
            brands = models.Brands.objects.get(id=brands_id)
            return render(req, self.template, context={
                'brand': brands
            })
        else:
            return render(req, self.template)

    def post(self, req, brands_id=None):

        name = req.POST['name']
        slug = req.POST['slug']
        description = req.POST['description']

        if brands_id:
            brands_id = int(brands_id)
            brand = models.Brands.objects.get(id=brands_id)
            brand.name = name
            brand.slug = slug
            brand.description = description
            brand.save()
            msg = "Record Updated [" + "Brand id: " + str(brand.id) +  "]"
        else:
            brand = models.Brands(
                name=name,
                slug=slug,
                description=description
            )
            brand.save()
            msg = "Successfully saved [" + "Brands id: " + str(brand.id) + "]"

        return render(req, self.template, context={
            'msg': msg,
            'brand': brand
        })

def BrandsListView(req):
    brands = models.Brands.objects.all()
    return render(req, 'ecom_app/brands_list.html', context={
        'brands': brands
    })

def BrandsViewView(req, brands_id):
    template = "ecom_app/brands_view.html"
    brands_id = int(brands_id)
    brand = models.Brands.objects.get(id=brands_id)
    return render(req, template, context={
        'brand': brand
    })

def BrandsDeleteView(req, brands_id):
    brands_id = int(brands_id)
    brand = models.Brands.objects.get(id=brands_id)
    brand.delete()
    return redirect("ecom_app:brands_list")