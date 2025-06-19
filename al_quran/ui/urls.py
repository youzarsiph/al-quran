"""URLConf for al_quran.ui"""

from django.contrib.auth import views as auth
from django.urls import path

from al_quran.ui import views

# Create your patterns here.
app_name = "al-quran"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("chapters/", views.ChapterListView.as_view(), name="chapters"),
    path("chapters/<int:pk>/", views.ChapterDetailView.as_view(), name="chapter"),
    path("parts/", views.PartListView.as_view(), name="parts"),
    path("parts/<int:pk>/", views.PartDetailView.as_view(), name="part"),
    path("groups/", views.GroupListView.as_view(), name="groups"),
    path("groups/<int:pk>/", views.GroupDetailView.as_view(), name="group"),
    path("quarters/", views.QuarterListView.as_view(), name="quarters"),
    path("quarters/<int:pk>/", views.QuarterDetailView.as_view(), name="quarter"),
    path("pages/", views.PageListView.as_view(), name="pages"),
    path("pages/<int:pk>/", views.PageDetailView.as_view(), name="page"),
] + [
    path("accounts/login/", auth.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth.LogoutView.as_view(), name="logout"),
    path("accounts/signup/", views.SignupView.as_view(), name="signup"),
    path("accounts/profile/", views.ProfileView.as_view(), name="profile"),
    path(
        "accounts/<int:pk>/update/", views.UserUpdateView.as_view(), name="update-user"
    ),
    path(
        "accounts/<int:pk>/delete/", views.UserDeleteView.as_view(), name="delete-user"
    ),
    path(
        "accounts/password/change/",
        auth.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password/change/done/",
        auth.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "accounts/password/reset/",
        auth.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password/reset/done/",
        auth.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/password/reset/<uidb64>/<token>/",
        auth.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/password/reset/complete/",
        auth.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
