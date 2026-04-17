from django.views.generic import ListView, TemplateView

from .models import DepartmentInfo


class HomeView(TemplateView):
    template_name = "core/home.html"


class DepartmentView(ListView):
    model = DepartmentInfo
    template_name = "core/department.html"
    context_object_name = "departments"
