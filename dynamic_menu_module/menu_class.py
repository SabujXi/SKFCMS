class Menu:
    def __init__(self, menu):
        self.menu_instance = menu
        self.children = []

    def get_menu(self):
        return self.menu_instance

    def get_children(self):
        return self.children

    def get_child(self, idx):
        return self.get_children()[idx]

    def get_child_count(self):
        return len(self.get_children())

    def has_children(self):
        if len(self.get_children()) == 0:
            return False
        else:
            return True

    def append_child(self, child):
        self.children.append(child)

    def get_parent_id(self):
        return self.get_menu().parent_id

    def get_menu_id(self):
        return self.get_menu().id

    def get_menu_name(self):
        return self.get_menu().name

    def __str__(self):
        return self.get_menu_html()

    def get_menu_html(self, list_type="ul", level=1):
        level += 1
        str_list = list()

        if self.has_children():
            str_list.append("<li>" + self.get_menu_name())
            # children html
            str_list.append("<" + list_type + ">")
            for menu in self.get_children():
                str_list.append(menu.get_menu_html(list_type=list_type))
            str_list.append("</" + list_type + ">")
            # < children html
            str_list.append("</li>")
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

    def get_menu_html(self, list_type="ul"):
        str_list = list()
        str_list.append("<" + list_type + ">")
        for child in self.get_children():
            str_list.append(child.get_menu_html(list_type=list_type))
        str_list.append("</" + list_type + ">")
        return "".join(str_list)
