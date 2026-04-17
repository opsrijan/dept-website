from django.urls import path

from .views import AlumniProfileListView

app_name = "alumni"

urlpatterns = [
    path("", AlumniProfileListView.as_view(), name="index"),
]
