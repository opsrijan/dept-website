from django.urls import path

from .views import TeamMemberListView

app_name = "team"

urlpatterns = [
    path("", TeamMemberListView.as_view(), name="index"),
]
