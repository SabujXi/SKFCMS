from ecom_app import models


# The context processor function
def site_settings(request):
    try:
        sets = models.SiteSetting.objects.get(pk=1)
    except sets.DoesNotExist:
        sets = None

    return {'sets': sets}