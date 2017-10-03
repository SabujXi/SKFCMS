class Menu:
    def __init__(self, menu):
        self.menu_instance = menu
        self.childreen = []
    def get_menu(self):
        return self.menu_instance
    def get_childreen(self):
        return self.childreen
    def add_child(self,child):
        self.childreen.append(child)
    def get_parent_id(self):
        return self.get_menu().parent__id
    def get_menu_id(self):
        return self.get_menu().id
    def get_menu_name(self):
        return self.get_menu().name
    def get_menu_html(self):
        return None
