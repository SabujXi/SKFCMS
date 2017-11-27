from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecom_app import models
from django.views import View


def cart_view(request):
    template = 'ecom_app/frontend/cart.html'
    if 'pids' in request.session:
        pids = request.session['pids']
    else:
        pids = []

    prods = models.Product.objects.filter(id__in=pids)

    title = 'Cart Page'
    context = {'title': title, 'prods': prods}
    return render(request, template, context)


def add2cart_view(request, pid=None):
    ref = request.META['HTTP_REFERER']

    if 'pids' not in request.session:
        l = request.session['pids'] = []
    else:
        l = request.session['pids']

    if pid not in l:
        l.append(pid)

    request.session['pids'] = l

    # if not request.user.is_authenticated:
    request.session.set_expiry(5)

    return redirect(ref)


def del4mcart_view(request, pid=None):
    ref = request.META['HTTP_REFERER']

    if 'pids' in request.session:
        l = request.session['pids']
        l.remove(pid)
        request.session['pids'] = l
    return redirect(ref)
