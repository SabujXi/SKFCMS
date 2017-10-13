from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from ecom_app import models
from django.views import View
from django import forms
# from dynamic_menu_module.menu import Menu
from ecom_app.forms.menu_form import MenuForm
from django.db.models import Q
from django.contrib import messages

class CreateEditMenuView(View):
    template = 'ecom_app/backend/menu_form.html'

    def parent_choice_builder(self, Q):
        choices = [("-1", "----")]
        for x in Q:
            choices.append(
                (x.id, x.name)
            )
        return choices

    def get(self, req: HttpRequest, menu_id=None): # type hinted req
        do_edit = False

        if menu_id:
            print("Menu Id: ", menu_id)
            menu_id = int(menu_id)
            try:
                menu = models.MenuModel.objects.get(pk=menu_id)
            except models.MenuModel.DoesNotExist:
                menu = None
        else:
            menu = None

        if menu:
            do_edit = True
            form = MenuForm({
                "name": menu.name,
                "description": menu.description,
                "type": menu.type,
                "content": menu.content,
                "serial_no": menu.serial_no,
                "parent": menu.parent,
                "disabled": menu.disabled
            })
        else:
            form = MenuForm()

        if not do_edit:
            menus = models.MenuModel.objects.all()
            parent_choices = self.parent_choice_builder(menus)
            form.fields["parent"] = forms.ChoiceField(required=False, choices=parent_choices, label="Select Parent")
        else:
            menus = models.MenuModel.objects.filter(~Q(parent=menu_id))
            parent_choices = self.parent_choice_builder(menus)
            form.fields["parent"] = forms.ChoiceField(required=False, choices=parent_choices, label="Select Parent")
        # print(dir(form))
        return render(req, self.template, context={
            'menu_form': form,
            "menu_id": menu_id
        })

    def post(self, req: HttpRequest, menu_id=None):
        if menu_id:
            menu_id = int(menu_id)
            menu = models.MenuModel.objects.get(pk=menu_id)
        else:
            menu = models.MenuModel()

        # building choices
        if not menu_id:
            menus = models.MenuModel.objects.all()
            parent_choices = self.parent_choice_builder(menus)
            form = MenuForm(req.POST)
            form.fields["parent"] = forms.ChoiceField(required=False, choices=parent_choices, label="Select Parent")
        else:
            menus = models.MenuModel.objects.filter(~Q(parent=menu_id))
            parent_choices = self.parent_choice_builder(menus)
            form = MenuForm(req.POST)
            form.fields["parent"] = forms.ChoiceField(required=False, choices=parent_choices, label="Select Parent")
        # < building choices

        if not form.is_valid():
            return render(req, self.template, context={
                'menu_form': form,
                "menu_id": menu_id
            })

        else:
            cd = form.cleaned_data
            name = cd["name"]
            description = cd["description"]
            m_type = cd["type"]
            content = cd["content"]
            serial_no = cd["serial_no"]
            parent = cd["parent"]
            disabled = cd["disabled"]
            menu.name = name
            menu.description = description
            menu.type = m_type

            # > content block

            menu.content = content
            # < content block

            menu.serial_no = serial_no

            if parent != "-1" and parent != "":
                parent_id = int(parent)
                parent = models.MenuModel.objects.get(pk=parent_id)
                menu.parent = parent

            menu.disabled = disabled
            menu.save()

            return redirect("ecom_app:create_edit_menu", menu.id)

"""
menus = models.MenuModel.objects.all()
menus = list(menus)
"""
def menu_list_view(request):
    template='ecom_app/backend/menu_list.html'
    title='Menu List'
    heading='Menu List'
    menus=models.MenuModel.objects.all()

    # test purpose
    random_content = ""
    from dynamic_menu_module.menu import menu_processor
    menu_root = menu_processor(menus)
    random_content = str(menu_root)
    # < test purpose

    context={'title':title, 'heading':heading, 'menus':menus, "random_content": random_content}

    return render(request, template, context)

def menu_delete_view(request, menu_id = None):
    models.MenuModel.objects.get(pk=menu_id).delete()
    messages.info(request, "Menu successfully deleted with id %s." % menu_id)
    return redirect("ecom_app:menu-list")