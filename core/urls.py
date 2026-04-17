from django.urls import path

from .views import DepartmentView, HomeView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("department/", DepartmentView.as_view(), name="department"),
]
