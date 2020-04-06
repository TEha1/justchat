from django.contrib import admin
from django.utils.html import format_html

from . import models
# Register your models here.

@admin.register(models.Message)
class Messagedmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'content', 'timestamp', 'manage_buttons']

    def manage_buttons(self, obj):
        return format_html('<a href="{}/change/">{}</a>'' -'
                           ' ''<a href="{}/delete/">{}</a>'.
                           format(obj.id, ('update'), obj.id, ('delete')))

    manage_buttons.short_description = ('Manage')
    manage_buttons.allow_tags = True