from django.urls import path

from .views import LeaderboardEntryListView

app_name = "leaderboard"

urlpatterns = [
    path("", LeaderboardEntryListView.as_view(), name="index"),
]
