"""URLConf for al_quran.ui"""

from django.urls import path

from al_quran.ui import views


# Create your patterns here.
app_name = "al-quran"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("chapters/", views.ChapterListView.as_view(), name="chapters"),
    path(
        "chapters/<int:pk>/", views.ChapterDetailView.as_view(), name="chapter-details"
    ),
    path("parts/", views.PartListView.as_view(), name="parts"),
    path("parts/<int:pk>/", views.PartDetailView.as_view(), name="part-details"),
    path("groups/", views.GroupListView.as_view(), name="groups"),
    path("groups/<int:pk>/", views.GroupDetailView.as_view(), name="group-details"),
    path("quarters/", views.QuarterListView.as_view(), name="quarters"),
    path(
        "quarters/<int:pk>/", views.QuarterDetailView.as_view(), name="quarter-details"
    ),
]
