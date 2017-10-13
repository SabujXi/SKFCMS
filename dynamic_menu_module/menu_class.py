class Menu:
    def __init__(self, menu):
        self.menu_instance = menu
        self.children = []

    def get_menu(self):
        return self.menu_instance

    def get_childreen(self):
        return self.children

    def get_child(self, idx):
        return self.get_childreen()[idx]

    def get_child_count(self):
        return len(self.get_childreen())

    def append_child(self,child):
        self.children.append(child)

    def get_parent_id(self):
        return self.get_menu().parent_id

    def get_menu_id(self):
        return self.get_menu().id

    def get_menu_name(self):
        return self.get_menu().name

    def __str__(self):
        return self.get_menu_html()

    # def get_menu_html(self):
    #     raise NotImplemented

    def get_menu_html(self, list_type="ol"):
        str_list = []

        if self.get_child_count() > 0:
            # children html
            str_list.append("<" + list_type + ">")
            for menu in self.get_childreen():
                str_list.append("<li>" + menu.get_menu_name() + menu.get_menu_html(list_type=list_type) + "</li>")
            str_list.append("</" + list_type + ">")
            # < children html
        else:
            str_list.append("<li>" + self.get_menu_name() + "</li>")


        return "".join(str_list)


class MenuRoot:
    def __init__(self, root_menus):
        self.children = root_menus

    def get_children(self):
        return self.children

    def __str__(self):
        return self.get_menu_html()

    def get_menu_html(self, list_type="ol"):
        values = []
        values.append("<"+ list_type +">")
        for child in self.get_children():
            values.append(child.get_menu_html(list_type="ol"))
        values.append("</" + list_type + ">")
        return "".join(values)