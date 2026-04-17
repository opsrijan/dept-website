from django.views.generic import ListView

from .models import Opportunity


class OpportunityListView(ListView):
    model = Opportunity
    template_name = "opportunities/index.html"
    context_object_name = "opportunities"
