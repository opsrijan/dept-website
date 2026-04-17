from django.urls import path

from .views import PlacementRecordListView

app_name = "placements"

urlpatterns = [
    path("", PlacementRecordListView.as_view(), name="index"),
]
