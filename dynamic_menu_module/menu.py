from dynamic_menu_module.menu_class import Menu


def menu_processor(menu_list):
    root_menus = []
    non_root_menus = []

    for mnu in menu_list:
        if mnu.parent == None:
            root_menus.append(mnu)
        else:
            non_root_menus.append(mnu)

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
    xxx = ''
    # for x in non_root_menus_obj:
    #     if x.get_parent_id() != None:
    #         xxx = xxx + ' , ' + str(x.get_parent_id())

    processed_menus_map = {}
    for rmo in root_menu_objs:
        processed_menus_map[ rmo.get_menu_id() ] = rmo

    for nrmo in non_root_menu_objs:
        parent_id = nrmo.get_parent_id()
        if parent_id in processed_menus_map:
            processed_menu = processed_menus_map[parent_id]
            processed_menu.add_child(nrmo)
