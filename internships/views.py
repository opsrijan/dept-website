from django.views.generic import ListView

from .models import InternshipOpportunity


class InternshipOpportunityListView(ListView):
    model = InternshipOpportunity
    template_name = "internships/index.html"
    context_object_name = "internships"
