from django import forms
from ecom_app.models.choices.choices import menu_type_choices


class MenuForm(forms.Form):
    def __init__(self, parent_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'] = forms.ChoiceField(required=False, choices=parent_choices, label="Select Parent")

    name = forms.CharField(required=True, max_length=64, label="Name", widget=forms.TextInput(attrs={'class': 'jhogra jhati', 'id': 'para'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'classy-editor'}), label="Description")
    type = forms.ChoiceField(required=True, choices=menu_type_choices, label="Menu Type")
    content = forms.CharField(required=True, label="Content")
    serial_no = forms.IntegerField(required=True, initial=0, label="Sorting Order")
    parent = forms.ChoiceField(required=False, label="Select Parent")
    disabled = forms.BooleanField(required=False, initial=False, label="Is Disabled?")
