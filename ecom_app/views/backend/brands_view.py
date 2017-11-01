from django.shortcuts import render, redirect
from ecom_app import models
from django.views import View


class BrandsCreateOrEditView(View):
    template = 'ecom_app/backend/brands_form.html'
    heading = 'Brand Form'

    def get(self, req, brand_id=None):
        if brand_id:
            brand_id = int(brand_id)
            brand = models.Brands.objects.get(id=brand_id)
            return render(req, self.template, context={
                'brand': brand, 'heading': self.heading
            })
        else:
            return render(req, self.template, context={
                'heading': self.heading
            })

    def post(self, req, brand_id=None):

        name = req.POST['name']
        slug = req.POST['slug']
        description = req.POST['desc']

        if brand_id:
            brand_id = int(brand_id)
            brand = models.Brands.objects.get(id=brand_id)
            brand.name = name
            brand.slug = slug
            brand.description = description
            brand.save()
            msg = "Record Updated [" + "Brand id: " + str(brand.id) + "]"
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
            'brand': brand,
            'heading': self.heading
        })


def BrandsListView(req):
    brands = models.Brands.objects.all()
    return render(req, 'ecom_app/backend/brands_list.html', context={
        'brands': brands,
        'heading': 'Brands List'
    })

'''
def BrandsViewView(req, brand_id):
    template = "ecom_app/brands_view.html"
    brand_id = int(brand_id)
    brand = models.Brands.objects.get(id=brand_id)
    return render(req, template, context={
        'brand': brand
    })
'''

def BrandsDeleteView(req, brand_id):
    brand_id = int(brand_id)
    brand = models.Brands.objects.get(id=brand_id)
    brand.delete()
    return redirect("ecom_app:brands_list")
