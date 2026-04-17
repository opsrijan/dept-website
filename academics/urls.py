from django.urls import path

from .views import AcademicProgramListView

app_name = "academics"

urlpatterns = [
    path("", AcademicProgramListView.as_view(), name="index"),
]
