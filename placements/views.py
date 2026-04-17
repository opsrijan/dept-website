from django.views.generic import ListView

from .models import PlacementRecord


class PlacementRecordListView(ListView):
    model = PlacementRecord
    template_name = "placements/index.html"
    context_object_name = "placements"
