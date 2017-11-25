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
    UserLogin,
    logout_view,
    forgot_pass,
    reset_pass,
    verify_email_view
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
    CrudCategory, category_list_view, category_delete,
)

from ecom_app.views.backend.product_view import (
    CrudProduct, CrudProductTabular, product_list_view, product_single_view, product_delete, TestProductCrudViewForFormset
)

from ecom_app.views.backend.brands_view import (
    BrandsCreateOrEditView, BrandsListView, BrandsDeleteView, #BrandsViewView,
)


from ecom_app.views.backend.user_view import (
    BackendUserLogin, CrudUser, user_list_view, backend_logout_view
)

from ecom_app.views.backend.menu_views import (
    CreateEditMenuView, menu_list_view, menu_delete_view
)

from ecom_app.views.frontend.upload_file_provider import upload_file_provider_view

# http error view

from ecom_app.views import http_error_views

urlpatterns = [

    # url pattern for main url
    url(r'^$', front_index_view, name='front-index'),
    url(r'^category/(?P<cat_id>[0-9]*)$', category_porduct_view, name='cat-product'),
    url(r'^brands/(?P<brand_id>[0-9]*)$', brand_porduct_view, name='brand-product'),
    url(r'^product-details/(?P<prod_id>[0-9]*)$', porduct_details_view, name='product-details'),
    url(r'^cart/$', cart_view, name='cart'),
    url(r'^checkout/$', checkout_view, name='checkout'),
    url(r'^reg/$', UserReg.as_view(), name='reg'),
    url(r'^email-ver/(?P<token>[a-zA-Z0-9_-]+)$', verify_email_view, name='email-verification'),
    url(r'^login/$', UserLogin.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^forgot-pass/$', forgot_pass, name='forgot-pass'),
    url(r'^reset-pass/(?P<token>[a-zA-Z0-9_-]+)$', reset_pass, name='reset-pass'),
    url(r'^contact/$', contact_view, name='contact'),

    url(r'^dashboard/$', back_index_view, name='back-index'),
    url(r'^settings/(?P<site_id>[0-9]*)$', CrudSiteSetting.as_view(), name='site-settings'),



    # url pattern for category
    url(r'^cat-form/(?P<cat_id>[0-9]*)$', CrudCategory.as_view(), name='cat-form'),
    url(r'^cat-list/$', category_list_view, name='cat-list'),
    url(r'^cat-delete/([0-9]+)$', category_delete, name='cat-delete'),

    # url pattern for product
    url(r'^prod-form/(?P<prod_id>[0-9]*)$', CrudProduct.as_view(), name='prod-form'),
    url(r'^prod-form-tabular/(?P<prod_id>[0-9]*)$', CrudProductTabular.as_view(), name='prod-form-tabular'),
    url(r'^prod-list/$', product_list_view, name='prod-list'),
    url(r'^prod-single/([0-9]+)$', product_single_view, name='prod-single'),
    url(r'^prod-del/([0-9]+)$', product_delete, name='prod-del'),
    url(r'^formset$', TestProductCrudViewForFormset.as_view(), name='prod-formset'),

    # url pattern for brands
    url(r'^brand-form/(?P<brand_id>[0-9]*)$', BrandsCreateOrEditView.as_view(), name='brand-form'),
    url(r'^brand-list/$', BrandsListView, name='brand-list'),
    #url(r'^brand-view/([0-9]+)$', BrandsViewView, name='brand-view'),
    url(r'^brand-delete/([0-9]+)$', BrandsDeleteView, name='brand-delete'),


    # url pattern for Users
    url(r'^admin/$', BackendUserLogin.as_view(), name='user-login'),
    url(r'^user-logout/$', backend_logout_view, name='user-logout'),
    url(r'^user-form/(?P<user_id>[0-9]*)$', CrudUser.as_view(), name='user-form'),
    url(r'^user-list/$', user_list_view, name='user-list'),

    #url(r'^supplier-delete/([0-9]+)$', SuppliersDeleteView, name='suppliers-delete'),

    # url(r'^menu/$', menu_views, name='menu'),
    url(r'^menu-list$', menu_list_view, name='menu-list'),
    url(r'^menu-delete/(?P<menu_id>[0-9]+)$', menu_delete_view, name='delete_menu'),
    url(r'^create-edit-menu/(?P<menu_id>[0-9]*)$', CreateEditMenuView.as_view(), name='create_edit_menu'),
    url(r'^upload_dir/(?P<file_path>.*)', upload_file_provider_view, name="upload_file_provider")

]



