from django import template
from app_menu.models import MenuItem

register = template.Library()


class MenuItemNode:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.active = False
        self.children = []


def find_active_menu_items(path, menu_item):
    item = MenuItemNode(menu_item.name, menu_item.url)

    if menu_item.url == path:
        item.active = True

    if menu_item.get_children:
        for child in menu_item.get_children():
            child_item = find_active_menu_items(path, child)
            item.children.append(child_item)
            if child_item.active:
                item.active = True

    return item


@register.inclusion_tag('app_menu/menu.html', takes_context=True)
def show_top_menu(context, menu_type=None):
    menu_items_raw = MenuItem.objects.filter(menu__name=menu_type, level=0).select_related('menu')
    menu = []
    for item in menu_items_raw:
        menu.append(find_active_menu_items(path=context.request.path, menu_item=item))

    print(menu)

    return {
        "menu_items": menu,
        "cur_page": context.request.path,
        "test": "test"
    }
