from django.urls import path
from django.views.generic import TemplateView
from .views import ProfessorListView

app_name = 'academics'   # ← THIS line is mandatory

urlpatterns = [
    path('', TemplateView.as_view(template_name='academics/index.html'), name='index'),
    path('professors/', ProfessorListView.as_view(), name='professors'),
]