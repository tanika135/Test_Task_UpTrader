from django import template
from app_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('app_menu/menu.html')
def show_top_menu(menu_type=None):
    menu_items = MenuItem.objects.filter(menu__name=menu_type).select_related('menu')
    return {
        "menu_items": menu_items,
    }
