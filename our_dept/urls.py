from django.urls import path

app_name = 'our_dept'

from .views import StudentListView, PhDStudentListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='students'),
    path('phd/', PhDStudentListView.as_view(), name='phd'),   # ← add this
]