from django.contrib import admin

from .models import GalleryItem


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("title", "event_name", "event_date")
    list_filter = ("event_name",)
    search_fields = ("title", "event_name")
