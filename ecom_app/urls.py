from django.conf.urls import url
from . import views

# Frontend Part
from ecom_app.views.frontend.index_view import (
    front_index_view,
)

from ecom_app.views.frontend.product_view import (
    category_porduct_view, brand_porduct_view, porduct_details_view,
)

from ecom_app.views.frontend.cart_view import (
    cart_view,
)

from ecom_app.views.frontend.checkout_view import (
    checkout_view,
)

from ecom_app.views.frontend.users_login_view import (
    UserReg,
)

from ecom_app.views.frontend.contact_view import (
    contact_view,
)

# Backend Part
from ecom_app.views.backend.index_view import (
    back_index_view
)

from ecom_app.views.backend.backend_settings_view import (CrudSiteSetting)

from ecom_app.views.backend.category_view import (
    CrudCategory, category_list_view, category_single_view, category_conf_del, category_delete,
)

from ecom_app.views.backend.product_view import (
    CrudProduct, CrudProductTabular, product_list_view, product_single_view, product_delete,
)

from ecom_app.views.backend.brands_view import (
    BrandsCreateOrEditView, BrandsListView, BrandsViewView, BrandsDeleteView
)

from ecom_app.views.backend.suppliers_view import (
    SuppliersCreateOrEditView, SuppliersListView, SuppliersDeleteView
)

from ecom_app.views.backend.user_view import (
    CrudUser, UserListView,
)

from ecom_app.views.backend.menu_views import (
    CreateEditMenuView, menu_list_view, menu_delete_view
)

from ecom_app.views.frontend.upload_file_provider import upload_file_provider_view

urlpatterns = [

    # url pattern for main url
    url(r'^$', front_index_view, name='front-index'),
    url(r'^category/(?P<cat_id>[0-9]*)$', category_porduct_view, name='cat-product'),
    url(r'^brands/(?P<brand_id>[0-9]*)$', brand_porduct_view, name='brand-product'),
    url(r'^product-details/$', porduct_details_view, name='product-details'),
    url(r'^cart/$', cart_view, name='cart'),
    url(r'^checkout/$', checkout_view, name='checkout'),
    url(r'^login/(?P<user_id>[0-9]*)$', UserReg.as_view(), name='login'),
    url(r'^contact/$', contact_view, name='contact'),

    url(r'^admin/$', back_index_view, name='back-index'),
    url(r'^settings/(?P<site_id>[0-9]*)$', CrudSiteSetting.as_view(), name='site-settings'),

    # url pattern for Social Link
    #url(r'^social/$', front_social_view, name='social'),

    # url pattern for category
    url(r'^cat-form/(?P<cat_id>[0-9]*)$', CrudCategory.as_view(), name='cat-form'),
    url(r'^cat-list/$', category_list_view, name='cat-list'),
    url(r'^cat-single/([0-9]+)$', category_single_view, name='cat-single'),
    url(r'^cat-del-conf/([0-9]+)$', category_conf_del, name='cat-conf-del'),
    url(r'^cat-delete/([0-9]+)$', category_delete, name='cat-delete'),

    # url pattern for product
    url(r'^prod-form/(?P<prod_id>[0-9]*)$', CrudProduct.as_view(), name='prod-form'),
    url(r'^prod-form-tabular/(?P<prod_id>[0-9]*)$', CrudProductTabular.as_view(), name='prod-form-tabular'),
    url(r'^prod-list/$', product_list_view, name='prod-list'),
    url(r'^prod-single/([0-9]+)$', product_single_view, name='prod-single'),
    url(r'^prod-del/([0-9]+)$', product_delete, name='prod-del'),

    # url pattern for brands
    url(r'^brand-form/(?P<brands_id>[0-9]*)$', BrandsCreateOrEditView.as_view(), name='brands-form'),
    url(r'^brand-list/$', BrandsListView, name='brands-list'),
    url(r'^brand-view/([0-9]+)$', BrandsViewView, name='brands_view'),
    url(r'^brand-delete/([0-9]+)$', BrandsDeleteView, name='brands_delete'),

    # url pattern for suppliers
    url(r'^supplier-form/(?P<suppliers_id>[0-9]*)$', SuppliersCreateOrEditView.as_view(), name='suppliers-form'),
    url(r'^supplier-list/$', SuppliersListView, name='suppliers-list'),
    url(r'^supplier-delete/([0-9]+)$', SuppliersDeleteView, name='suppliers-delete'),

    # url pattern for Users
    url(r'^user-form/(?P<user_id>[0-9]*)$', CrudUser.as_view(), name='user-form'),
    url(r'^user-list/$', UserListView, name='user-list'),
    #url(r'^supplier-delete/([0-9]+)$', SuppliersDeleteView, name='suppliers-delete'),

    # url(r'^menu/$', menu_views, name='menu'),
    url(r'^menu-list$', menu_list_view, name='menu-list'),
    url(r'^menu-delete/(?P<menu_id>[0-9]+)$', menu_delete_view, name='delete_menu'),
    url(r'^create-edit-menu/(?P<menu_id>[0-9]*)$', CreateEditMenuView.as_view(), name='create_edit_menu'),
    url(r'^upload_dir/(?P<file_path>.*)', upload_file_provider_view, name="upload_file_provider")
]
