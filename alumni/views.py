from django.views.generic import ListView

from .models import AlumniProfile


class AlumniProfileListView(ListView):
    model = AlumniProfile
    template_name = "alumni/index.html"
    context_object_name = "alumni_profiles"
