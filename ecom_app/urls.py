from django.conf.urls import url
#from . import views

from ecom_app.views.index_view import (
	front_index_view,
	back_index_view,
	product_menu_view,
	category_menu_view,
	)
from ecom_app.views.category_view import (
	CrudCategory,
	category_list_view,
	category_single_view,
	category_conf_del,
	category_delete,
	)

from ecom_app.views.product_view import (
	CrudProduct,
	product_list_view,
	product_single_view,
	product_delete,
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
    url(r'^$', front_index_view, name='front-index'),
    url(r'^admin/$', back_index_view, name='back-index'),

    url(r'^prod-menu/$', product_menu_view, name='prod-menu'),
    url(r'^cat-menu/$', category_menu_view, name='cat-menu'),

    url(r'^cat-form/(?P<cat_id>[0-9]*)$', CrudCategory.as_view(), name='cat-form'),
    url(r'^cat-list/$', category_list_view, name='cat-list'),
    url(r'^cat-single/([0-9]+)$', category_single_view, name='cat-single'),
    url(r'^cat-del-conf/([0-9]+)$', category_conf_del, name='cat-conf-del'),
    url(r'^cat-delete/([0-9]+)$', category_delete, name='cat-delete'),

    url(r'^prod-form/(?P<prod_id>[0-9]*)$', CrudProduct.as_view(), name='prod-form'),
    url(r'^prod-list/$', product_list_view, name='prod-list'),
    url(r'^prod-single/([0-9]+)$', product_single_view, name='prod-single'),
    url(r'^prod-del/([0-9]+)$', product_delete, name='prod-del'),
    
    
    
    url(r'^brand-form/(?P<brands_id>[0-9]*)$', BrandsCreateOrEditView.as_view(), name='brands_form'),
    url(r'^brand-list$', BrandsListView, name='brands_list'),
    url(r'^brand-view/([0-9]+)$', BrandsViewView, name='brands_view'),
    url(r'^brand-delete/([0-9]+)$', BrandsDeleteView, name='brands_delete'),
    url(r'^supplier-form/(?P<suppliers_id>[0-9]*)$', SuppliersCreateOrEditView.as_view(), name='suppliers_form'),
    url(r'^supplier-list$', SuppliersListView, name='suppliers_list'),
    url(r'^supplier-view/([0-9]+)$', SuppliersViewView, name='suppliers_view'),
    url(r'^supplier-delete/([0-9]+)$', SuppliersDeleteView, name='suppliers_delete'),
]