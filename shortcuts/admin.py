from django.contrib import admin
from shortcuts.models import Shortcut

class ShortcutAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('alias', 'redirect_to', 'method')
        }),
        ('HTML meta options', {
            'fields': ('interval', 'title', 'analytics')
        }),
    )
    list_display = ('alias', 'redirect_to', 'method')
    list_links = ('alias',)
    list_filter = ('method',)
    
admin.site.register(Shortcut, ShortcutAdmin)