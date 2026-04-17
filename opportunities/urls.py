from django.urls import path

from .views import OpportunityListView

app_name = "opportunities"

urlpatterns = [
    path("", OpportunityListView.as_view(), name="index"),
]
