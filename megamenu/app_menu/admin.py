from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from app_menu.models import MenuItem, MenuType


class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(MenuItem, MenuItemMPTTModelAdmin)


class MenuTypeAdmin(admin.ModelAdmin):
    model = MenuType


admin.site.register(MenuType, MenuTypeAdmin)
