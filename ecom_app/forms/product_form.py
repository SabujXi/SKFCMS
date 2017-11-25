from django import forms
from ecom_app.models.choices.choices import menu_type_choices


# class ProductForm(forms.Form):
#     image_file = forms.FileField()


class TabularProductForm(forms.Form):
    product_name = forms.CharField(label="Product Name")
    brand = forms.ChoiceField(label="Brand")

