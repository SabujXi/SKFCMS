from django.conf.urls import url

from ecom_app.views.index_views import index_view

from ecom_app.views.category_views import (
    category_form_view,
    category_list_view,
    CategoryCreateOrEditView,
    category_view_view,
    category_delete_view
)

from ecom_app.views.brands_views import (
	BrandsCreateOrEditView,
	BrandsListView,
	BrandsViewView,
	BrandsDeleteView
)

from ecom_app.views.suppliers_views import (
	SuppliersCreateOrEditView,
	SuppliersListView,
	SuppliersViewView,
	SuppliersDeleteView
)

urlpatterns = [
    url(r'^$', index_view,name='index'),
    url(r'^cat-form/(?P<cat_id>[0-9]*)$', CategoryCreateOrEditView.as_view(), name='cat_form'),
    url(r'^cat-list$', category_list_view, name='cat_list'),
    url(r'^cat-view/([0-9]+)$', category_view_view, name='cat_view'),
    url(r'^cat-delete/([0-9]+)$', category_delete_view, name='cat_delete'),
    url(r'^brand-form/(?P<brands_id>[0-9]*)$', BrandsCreateOrEditView.as_view(), name='brands_form'),
    url(r'^brand-list$', BrandsListView, name='brands_list'),
    url(r'^brand-view/([0-9]+)$', BrandsViewView, name='brands_view'),
    url(r'^brand-delete/([0-9]+)$', BrandsDeleteView, name='brands_delete'),
    url(r'^supplier-form/(?P<suppliers_id>[0-9]*)$', SuppliersCreateOrEditView.as_view(), name='suppliers_form'),
    url(r'^supplier-list$', SuppliersListView, name='suppliers_list'),
    url(r'^supplier-view/([0-9]+)$', SuppliersViewView, name='suppliers_view'),
    url(r'^supplier-delete/([0-9]+)$', SuppliersDeleteView, name='suppliers_delete'),
]