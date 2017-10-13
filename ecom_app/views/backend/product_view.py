from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View



# Create your views here.
class CrudProduct(View):
	template='ecom_app/backend/prod_form.html'
	title='Product Form'
	heading='Product Form'
	cats=models.Category.objects.all()
	brands=models.Brands.objects.all()
	suppliers=models.Suppliers.objects.all()
	
	
	def get(self, request, prod_id=None):
		if prod_id:
			prod_id=int(prod_id)
			prod=models.Product.objects.get(pk=prod_id)
			context={'prod':prod, 'cats':self.cats, 'brands':self.brands, 'suppliers':self.suppliers, 'title':self.title, 'heading':self.heading}

			return render(request, self.template, context)
		else:
			context={'cats':self.cats,'brands':self.brands, 'suppliers':self.suppliers, 'title':self.title, 'heading':self.heading}
			return render(request, self.template, context)
	
	def post(self, request, prod_id=None):
		name=request.POST.get('name','')
		desc=request.POST.get('desc','')
		short_desc=request.POST.get('short_desc','')
		price=request.POST.get('price','')
		discount=request.POST.get('discount','')
		imageurl=request.POST.get('imageurl','')
		category_ids=request.POST.getlist('category')
		brand=request.POST.get('brand')

		#print(category_ids)
		#category=request.POST.get('category','') This line for single category value

		# create cat objs...
		categories = [] #List for multiple category
		for cat_id_ in category_ids:
			cat_id = int(cat_id_)
			cat = models.Category.objects.get(pk=cat_id)
			categories.append(cat)
		# end create cat objs
		
		if prod_id:
			prod_id = int(prod_id)
			prod=models.Product.objects.get(pk=prod_id)
			
			prod.name=name
			prod.description=desc
			prod.short_description=short_desc
			prod.category=categories
			prod.price=price
			prod.discount=discount
			prod.imageurl=imageurl
			prod.brands_id=brand
			prod.save()
			#prod.category.related_set = categories
			msg='Data updated...'
			context={'cats':self.cats, 'prod':prod, 'suppliers':self.suppliers, 'msg':msg, 'title':self.title, 'heading':self.heading}
			return render(request, self.template, context)
		else:
			prod=models.Product(
							name=name,
							description=desc,
							short_description=short_desc,
							price=price,
							discount=discount,
							imageurl=imageurl,
							brands_id=brand
							)
			prod.save()
			prod.category.add(*categories)

			#prod.category.add(category) This line for single category value
			msg='Data inserted...'
			context={'cats':self.cats, 'msg':msg, 'suppliers':self.suppliers, 'title':self.title, 'heading':self.heading}
			return render(request, self.template, context)


def product_list_view(request):
	template='ecom_app/backend/prod_list.html'
	title='Product List'
	heading='Product List'
	prods=models.Product.objects.all()

	context={'prods':prods, 'title':title, 'heading':heading}

	return render(request, template, context)


def product_single_view(request, prod_id):
	prod_id=int(prod_id)
	template='ecom_app/backend/prod_single.html'
	title='Product Views'
	prod=models.Product.objects.get(id=prod_id)
	context={'prod':prod, 'title':title}
	return render(request, template, context)

'''
def prod_conf_del(request, prod_id):
	prod_id=int(prod_id)
	template='ecom_app/prod_del_conf.html'
	title='Are you sure to delete?'
	prods=models.prodegory.objects.get(id=prod_id)
	context={'prod':prods, 'title':title}
	return render(request, template, context)
'''

def product_delete(request, prod_id):
	template='ecom_app/backend/prod_list.html'
	prod_id=int(prod_id)
	if prod_id:
		prod=models.Product.objects.get(pk=prod_id)
		prod.delete()
		return redirect('ecom_app:prod-list')
		#return render(request, template, context)
