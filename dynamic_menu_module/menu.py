from dynamic_menu_module.menu_class import Menu, MenuRoot

def menu_processor(menu_list):
    root_menus = []
    non_root_menus = []

    # Classifying root and non root menus
    for mnu in menu_list:
        if mnu.parent_id == None:
            root_menus.append(mnu)
        else:
            non_root_menus.append(mnu)
    # < Classifying root and non root menus

    root_menu_objs = []
    non_root_menu_objs = []

    for rootmnu in root_menus:
        root_menu_objs.append(
                Menu(rootmnu)
            )

    for nonrootmnu in non_root_menus:
        non_root_menu_objs.append(
                Menu(nonrootmnu)
            )

    processed_menus_map = {}
    un_processed_menus_map = {}

    for rmo in root_menu_objs:
        processed_menus_map[ rmo.get_menu_id() ] = rmo
    for nrmo in non_root_menu_objs:
        un_processed_menus_map[ nrmo.get_menu_id() ] = nrmo

    _un_processed_menus_map = un_processed_menus_map.copy()
    while(len(un_processed_menus_map) != 0):
        for mid, nrmo in _un_processed_menus_map.items():
            parent_id = nrmo.get_parent_id()
            if parent_id in processed_menus_map:
                processed_menu = processed_menus_map[parent_id]
                processed_menu.append_child(nrmo)
                del un_processed_menus_map[mid]
                processed_menus_map[mid] = nrmo

    return MenuRoot(root_menu_objs)