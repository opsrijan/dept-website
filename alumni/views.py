from django.views.generic import TemplateView
from .models import Alumni


class AlumniListView(TemplateView):
    template_name = 'alumni/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['alumni']  = Alumni.objects.all()
        ctx['batches'] = (Alumni.objects
                          .values_list('batch', flat=True)
                          .distinct()
                          .order_by('-batch'))
        return ctx