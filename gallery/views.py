from django.views.generic import ListView

from .models import GalleryItem


class GalleryItemListView(ListView):
    model = GalleryItem
    template_name = "gallery/index.html"
    context_object_name = "gallery_items"
