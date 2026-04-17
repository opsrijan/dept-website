from django.urls import path

from .views import GalleryItemListView

app_name = "gallery"

urlpatterns = [
    path("", GalleryItemListView.as_view(), name="index"),
]
