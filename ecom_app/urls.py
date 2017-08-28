from django.conf.urls import url

from ecom_app.views.index_views import index_view

from ecom_app.views.category_views import (
    category_form_view,
    category_list_view,
    CategoryCreateOrEditView,
    category_view_view,
    category_delete_view
)

urlpatterns = [
    url(r'^$', index_view,name='index'),
    url(r'^cat-form/(?P<cat_id>[0-9]*)$', CategoryCreateOrEditView.as_view(), name='cat_form'),
    url(r'^cat-list$', category_list_view, name='cat_list'),
    url(r'^cat-view/([0-9]+)$', category_view_view, name='cat_view'),
    url(r'^cat-delete/([0-9]+)$', category_delete_view, name='cat_delete'),
]
