from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View


def category_porduct_view(request, cat_id=None):
    template = 'ecom_app/frontend/category_product.html'
    title = 'Category Products'
    products = models.Product.objects.filter(category=cat_id)
    category = models.Category.objects.get(pk=cat_id)
    context = {'products': products, 'category': category, 'title': title}
    return render(request, template, context)


def brand_porduct_view(request, brand_id=None):
    template = 'ecom_app/frontend/brands_product.html'
    title = 'Brand Products'
    products = models.Product.objects.filter(brand=brand_id)
    brand = models.Brands.objects.get(pk=brand_id)
    context = {'products': products, 'brand': brand, 'title': title}
    return render(request, template, context)


def porduct_details_view(request, prod_id=None):
    template = 'ecom_app/frontend/product_details.html'
    prod = models.Product.objects.get(pk=prod_id)
    title = 'Product Details'
    context = {'title': title, 'prod':prod}
    return render(request, template, context)
