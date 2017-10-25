from ecom_app import models


# The context processor function
def site_settings(request):
    try:
        sets = models.SiteSetting.objects.get(pk=1)
    except sets.DoesNotExist:
        sets = None

    return {'sets': sets}


def get_all_categories(request):
    categories = models.Category.objects.all()
    return {'categories': categories}


def get_all_brands(request):
    brands = models.Brands.objects.all()
    return {'brands': brands}
