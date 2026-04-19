from django.urls import path
from .views import AlumniListView

app_name = 'alumni'

urlpatterns = [
    path('', AlumniListView.as_view(), name='index'),
]