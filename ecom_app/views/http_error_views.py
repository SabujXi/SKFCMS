from django.shortcuts import render
from django.http.response import HttpResponseNotFound
from django.template import loader


def http_404_view(request):
    template = "ecom_app/404_page.html"
    template_obj = loader.get_template(template)
    text = template_obj.render()
    return HttpResponseNotFound(text)
