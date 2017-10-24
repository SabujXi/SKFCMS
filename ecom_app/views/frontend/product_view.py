from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View


def category_porduct_view(request, cat_id=None):
    template = 'ecom_app/frontend/category_product.html'
    title = 'Category Products'
    products = models.Product.objects.filter(category=cat_id)
    category = models.Category.objects.get(pk=cat_id)
    categories = models.Category.objects.all()
    brands = models.Brands.objects.all()
    context = {'products': products, 'categories': categories, 'category': category, 'brands': brands, 'title': title}
    return render(request, template, context)


def brand_porduct_view(request, brand_id=None):
    template = 'ecom_app/frontend/brands_product.html'
    title = 'Brand Products'
    products = models.Product.objects.filter(brands=brand_id)
    brand = models.Brands.objects.get(pk=brand_id)

    categories = models.Category.objects.all()
    brands = models.Brands.objects.all()
    context = {'products': products, 'categories': categories, 'brand': brand, 'brands': brands, 'title': title}
    return render(request, template, context)


def porduct_details_view(request):
    template = 'ecom_app/frontend/product_details.html'
    title = 'Product Details'
    context = {'title': title}
    return render(request, template, context)
