from django.views.generic import ListView
from .models import Student
from collections import OrderedDict

BATCH_LABELS = OrderedDict([
    
    ('2022-2026', '2022–2026'),
    ('2023-2027', '2023–2027'),
    ('2024-2028', '2024–2028'),
    ('2025-2029', '2025–2029'),
])

class StudentListView(ListView):
    model               = Student
    template_name       = 'our_dept/students.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_students = Student.objects.all().order_by('batch', 'roll_number')

        grouped = OrderedDict()
        for batch_key, batch_label in BATCH_LABELS.items():
            members = [s for s in all_students if s.batch == batch_key]
            if members:
                grouped[batch_label] = members

        context['grouped_students'] = grouped
        context['page_title'] = 'B.Tech Students'
        return context


from .models import PhDStudent

# Ordered dict of all possible PhD batches
# Sorted chronologically: Jul comes before Dec within same year
PHD_BATCH_ORDER = [
    'Jul 2021', 'Dec 2021',
    'Jul 2022', 'Dec 2022',
    'Jul 2023', 'Dec 2023',
    'Jul 2024', 'Dec 2024',
    'Jul 2025', 'Dec 2025',
]

class PhDStudentListView(ListView):
    model               = PhDStudent
    template_name       = 'our_dept/phd_students.html'
    context_object_name = 'phd_students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_students = PhDStudent.objects.all().order_by('name')

        grouped = OrderedDict()
        for batch in PHD_BATCH_ORDER:
            members = [s for s in all_students if s.batch == batch]
            if members:
                grouped[batch] = members

        context['grouped_students'] = grouped
        context['page_title'] = 'PhD Students'
        return context