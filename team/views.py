from django.views.generic import ListView

from .models import TeamMember


class TeamMemberListView(ListView):
    model = TeamMember
    template_name = "team/index.html"
    context_object_name = "members"
