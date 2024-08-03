from django.contrib import admin
from map.models import Map


class MapAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'main_image_url',
        'subscribed_count',
        'once_subscribed_count',
        'is_deleted',
        'created_by',
    ]


admin.site.register(Map, MapAdmin)
