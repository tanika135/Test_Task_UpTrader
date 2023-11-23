from django import template
from app_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('app_menu/menu.html', takes_context=True)
def show_top_menu(context):
    menu_items = MenuItem.objects.all()
    return {
        "menu_items": menu_items,
    }
