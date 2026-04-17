from django.views.generic import ListView

from .models import AcademicProgram


class AcademicProgramListView(ListView):
    model = AcademicProgram
    template_name = "academics/index.html"
    context_object_name = "programs"
