"""Views for al_quran.ui"""

from typing import Any, Dict

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from al_quran.core.chapters.models import Chapter
from al_quran.core.groups.models import Group
from al_quran.core.pages.models import Page
from al_quran.core.parts.models import Part
from al_quran.core.quarters.models import Quarter
from al_quran.ui import mixins
from al_quran.ui.forms import UserCreateForm

# User model
User = get_user_model()


# Create your views here.
class HomeView(generic.TemplateView):
    """Home page"""

    template_name = "ui/index.html"


class AboutView(generic.TemplateView):
    """About page"""

    template_name = "ui/about.html"


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    """Profile page"""

    template_name = "registration/profile.html"


# User views
class SignupView(SuccessMessageMixin, generic.CreateView):
    """Creates a user"""

    model = User
    form_class = UserCreateForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("al-quran:profile")
    success_message = "Your account was created successfully!"


class UserUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    mixins.AccountOwnerMixin,
    generic.UpdateView,
):
    """Updates a user"""

    model = User
    template_name = "registration/edit.html"
    fields = ["font", "theme", "interpretation", "translation", "transliteration"]
    success_url = reverse_lazy("al-quran:profile")
    success_message = "Your settings was updated successfully!"


class UserDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    mixins.AccountOwnerMixin,
    generic.DeleteView,
):
    """Deletes a user"""

    model = User
    template_name = "registration/delete.html"
    success_url = reverse_lazy("al-quran:index")
    success_message = "Your account was deleted successfully!"


class ChapterListView(FilterView, generic.ListView):
    """Displays all Chapters"""

    model = Chapter
    ordering = "id"
    paginate_by = 25
    template_name = "ui/list/chapters.html"
    filterset_fields = ["id", "order", "type", "verse_count", "page_count"]


class BaseDetailView:
    """Base view that provides extra context to template"""

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute pages and add it to context"""

        reverse = f"al-quran:{self.model._meta.model_name.lower()}"

        return {
            **super().get_context_data(**kwargs),
            "prev_url": reverse_lazy(reverse, args=[self.object.id - 1]),
            "next_url": reverse_lazy(reverse, args=[self.object.id + 1]),
        }


class ChapterDetailView(BaseDetailView, generic.DetailView):
    """Displays a Chapter"""

    model = Chapter
    template_name = "ui/detail/chapter.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute pages and add it to context"""

        return {
            **super().get_context_data(**kwargs),
            "pages": Page.objects.filter(verses__chapter_id=self.object.id)
            .distinct()
            .prefetch_related("verses"),
        }


class PartListView(FilterView, generic.ListView):
    """Displays all Parts"""

    model = Part
    ordering = "id"
    paginate_by = 15
    template_name = "ui/list/parts.html"
    filterset_fields = ["id", "verse_count", "page_count"]


class PartDetailView(BaseDetailView, generic.DetailView):
    """Displays a Part"""

    model = Part
    template_name = "ui/detail/part.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute pages and add it to context"""

        return {
            **super().get_context_data(**kwargs),
            "pages": Page.objects.filter(verses__part_id=self.object.id)
            .distinct()
            .prefetch_related("verses"),
        }


class GroupListView(FilterView, generic.ListView):
    """Displays all Groups"""

    model = Group
    ordering = "id"
    paginate_by = 30
    template_name = "ui/list/groups.html"
    filterset_fields = ["id", "part", "verse_count", "page_count"]


class GroupDetailView(BaseDetailView, generic.DetailView):
    """Displays a Group"""

    model = Group
    template_name = "ui/detail/group.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute pages and add it to context"""

        return {
            **super().get_context_data(**kwargs),
            "pages": Page.objects.filter(verses__group_id=self.object.id)
            .distinct()
            .prefetch_related("verses"),
        }


class QuarterListView(FilterView, generic.ListView):
    """Displays all Quarters"""

    model = Quarter
    ordering = "id"
    paginate_by = 60
    template_name = "ui/list/quarters.html"
    filterset_fields = ["id", "part", "group", "verse_count", "page_count"]


class QuarterDetailView(BaseDetailView, generic.DetailView):
    """Displays a Quarter"""

    model = Quarter
    template_name = "ui/detail/quarter.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute pages and add it to context"""

        return {
            **super().get_context_data(**kwargs),
            "pages": Page.objects.filter(verses__quarter_id=self.object.id)
            .distinct()
            .prefetch_related("verses"),
        }


class PageListView(FilterView, generic.ListView):
    """Displays all Pages"""

    model = Page
    ordering = "id"
    paginate_by = 100
    template_name = "ui/list/pages.html"
    filterset_fields = ["id", "chapter", "part", "group", "quarter", "verse_count"]
