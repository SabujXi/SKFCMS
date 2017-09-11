from django.shortcuts import render, redirect
from ecom_app import models
from django.views import View

class SuppliersCreateOrEditView(View):
    template = 'ecom_app/suppliers_form.html'

    def get(self, req, suppliers_id=None):
        if suppliers_id:
            suppliers_id = int(suppliers_id)
            suppliers = models.Suppliers.objects.get(id=suppliers_id)
            return render(req, self.template, context={
                'supplier': suppliers
            })
        else:
            return render(req, self.template)

    def post(self, req, suppliers_id=None):

        name = req.POST['name']
        slug = req.POST['slug']
        description = req.POST['description']

        if suppliers_id:
            suppliers_id = int(suppliers_id)
            supplier = models.Suppliers.objects.get(id=suppliers_id)
            supplier.name = name
            supplier.slug = slug
            supplier.description = description
            supplier.save()
            msg = "Record Updated [" + "Supplier id: " + str(supplier.id) +  "]"
        else:
            supplier = models.Suppliers(
                name=name,
                slug=slug,
                description=description
            )
            supplier.save()
            msg = "Successfully saved [" + "Suppliers id: " + str(supplier.id) + "]"

        return render(req, self.template, context={
            'msg': msg,
            'supplier': supplier
        })

def SuppliersListView(req):
    suppliers = models.Suppliers.objects.all()
    return render(req, 'ecom_app/suppliers_list.html', context={
        'suppliers': suppliers
    })

def SuppliersViewView(req, suppliers_id):
    template = "ecom_app/suppliers_view.html"
    suppliers_id = int(suppliers_id)
    supplier = models.Suppliers.objects.get(id=suppliers_id)
    return render(req, template, context={
        'supplier': supplier
    })

def SuppliersDeleteView(req, suppliers_id):
    suppliers_id = int(suppliers_id)
    supplier = models.Suppliers.objects.get(id=suppliers_id)
    supplier.delete()
    return redirect("ecom_app:suppliers_list")