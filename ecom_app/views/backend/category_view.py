from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View


# Create your views here.

class CrudCategory(View):
    template = 'ecom_app/backend/cat_form.html'
    title = 'Category Form'

    def get(self, request, cat_id):

        if cat_id:
            cat_id = int(cat_id)
            cat = models.Category.objects.get(id=cat_id)
            context = {
                'cat': cat,
                'title': self.title
            }
            return render(request, self.template, context)
        else:
            return render(request, self.template, context={'title': self.title})

    def post(self, request, cat_id):

        name = request.POST.get('name', '')
        slug = request.POST.get('slug', '')
        desc = request.POST.get('desc', '')

        if cat_id:

            cat_id = int(cat_id)
            cat = models.Category.objects.get(id=cat_id)
            cat.name = name
            cat.slug = slug.lower()
            cat.description = desc
            cat.save()
            msg = "Data Updated. Category : " + cat.name

        else:
            cat = models.Category(
                name=name,
                slug=slug.lower(),
                description=desc
            )
            cat.save()
            msg = "Data Saved."

        return render(request, self.template, context={'cat': cat, 'msg': msg, 'title': self.title})


'''
def cat_form_view(request, cat_id):
	template='ecom_app/cat_form.html'
	title='Category Form'
	
	if request.method=='GET':
		if cat_id:
			cat_id=int(cat_id)
			cat=models.Category.objects.get(id=cat_id)
			context={
				'cat':cat
			}
			return render(request, template, context)
		else:
			return render(request, template)

	elif request.method=='POST':
		name=request.POST.get('name', '')
		slug=request.POST.get('slug', '')
		desc=request.POST.get('desc', '')
		
		if cat_id:

			cat_id=int(cat_id)
			cat=models.Category.objects.get(id=cat_id)
			cat.name=name
			cat.slug=slug.lower()
			cat.description=desc
			cat.save()
			msg="Data Updated. Category : "+cat.name

		else:
			cat=models.Category(
				name=name,
				slug=slug.lower(),
				description=desc
				)
			cat.save()
			msg="Data Saved."

		return render(request, template, context={'cat':cat, 'msg':msg})
'''


def category_list_view(request):
    template = 'ecom_app/backend/cat_list.html'
    title = 'Category List'
    heading = 'Category List'
    cats = models.Category.objects.all()

    context = {'cats': cats, 'title': title, 'heading': heading}

    return render(request, template, context)


def category_single_view(request, cat_id):
    cat_id = int(cat_id)
    template = 'ecom_app/backend/cat_single.html'
    title = 'Category Views'
    cats = models.Category.objects.get(id=cat_id)
    context = {'cat': cats, 'title': title}
    return render(request, template, context)


def category_conf_del(request, cat_id):
    cat_id = int(cat_id)
    template = 'ecom_app/backend/cat_del_conf.html'
    title = 'Are you sure to delete?'
    cats = models.Category.objects.get(id=cat_id)
    context = {'cat': cats, 'title': title}
    return render(request, template, context)


def category_delete(request, cat_id):
    template = 'ecom_app/backend/cat_list.html'
    cat_id = int(cat_id)
    if cat_id:
        cats = models.Category.objects.get(id=cat_id)
        cats.delete()
        return redirect('ecom_app:cat-list')
