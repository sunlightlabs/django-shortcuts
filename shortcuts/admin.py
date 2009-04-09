from django.contrib import admin
from shortcuts.models import Shortcut

class ShortcutAdmin(admin.ModelAdmin):
    list_display = ('alias','redirect','uses_analytics')
    list_links = ('alias',)
    
admin.site.register(Shortcut, ShortcutAdmin)