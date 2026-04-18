from django.views.generic import TemplateView
from .models import GalleryImage

class GalleryListView(TemplateView):
    template_name = 'gallery/index.html'

    def get_context_data(self, **kwargs):
        ctx  = super().get_context_data(**kwargs)
        ctx['images'] = GalleryImage.objects.all()
        ctx['years']  = (GalleryImage.objects
                         .values_list('year', flat=True)
                         .distinct()
                         .order_by('-year'))
        return ctx