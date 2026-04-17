from django.views.generic import ListView

from .models import LeaderboardEntry


class LeaderboardEntryListView(ListView):
    model = LeaderboardEntry
    template_name = "leaderboard/index.html"
    context_object_name = "entries"
