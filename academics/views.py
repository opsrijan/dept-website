from django.views.generic import ListView

from .models import AcademicProgram


class AcademicProgramListView(ListView):
    model = AcademicProgram
    template_name = "academics/index.html"
    context_object_name = "programs"


from .models import Professor


class ProfessorListView(ListView):
    model = Professor
    template_name = 'academics/professors.html'
    context_object_name = 'professors'
    queryset = Professor.objects.all()