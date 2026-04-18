from django.contrib import admin
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display  = ('title', 'year', 'category')
    list_filter   = ('year', 'category')
    search_fields = ('title',)