from django.urls import path

from .views import InternshipOpportunityListView

app_name = "internships"

urlpatterns = [
    path("", InternshipOpportunityListView.as_view(), name="index"),
]
