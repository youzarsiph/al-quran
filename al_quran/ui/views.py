"""Views for al_quran.ui"""

from typing import Any, Dict
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from al_quran.comp.collections.models import Collection
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
    mixins.ExtraContextMixin,
    generic.UpdateView,
):
    """Updates a user"""

    model = User
    template_name = "registration/form.html"
    fields = ["font", "theme", "interpretation", "translation", "transliteration"]
    success_url = reverse_lazy("al-quran:profile")
    success_message = "Your settings was updated successfully!"
    extra_context = {"title": "Settings"}


class UserDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    mixins.AccountOwnerMixin,
    mixins.ExtraContextMixin,
    generic.DeleteView,
):
    """Deletes a user"""

    model = User
    template_name = "registration/form.html"
    success_url = reverse_lazy("al-quran:index")
    success_message = "Your account was deleted successfully!"
    extra_context = {
        "title": "Delete Account",
        "description": "Are you sure that you want to delete your account?",
    }


class ChapterListView(generic.ListView):
    """Displays all Chapters"""

    model = Chapter
    paginate_by = 25
    template_name = "ui/list/chapters.html"


class ChapterDetailView(generic.DetailView):
    """Displays a Chapter"""

    model = Chapter
    queryset = Chapter.objects.prefetch_related("pages")
    template_name = "ui/detail/chapter.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute page_list and add it to context"""

        return {
            **super().get_context_data(**kwargs),
            "prev_id": self.object.id - 1,
            "next_id": self.object.id + 1,
            "pages": Page.objects.filter(verses__chapter_id=self.object.id).distinct(),
        }


class PartListView(generic.ListView):
    """Displays all Parts"""

    model = Part
    paginate_by = 15
    template_name = "ui/list/parts.html"


class PartDetailView(generic.DetailView):
    """Displays a Part"""

    model = Part
    queryset = Part.objects.prefetch_related("pages")
    template_name = "ui/detail/part.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute page_list and add it to context"""

        return {
            **super().get_context_data(**kwargs),
            "prev_id": self.object.id - 1,
            "next_id": self.object.id + 1,
            "pages": Page.objects.filter(verses__part_id=self.object.id).distinct(),
        }


class GroupListView(generic.ListView):
    """Displays all Groups"""

    model = Group
    paginate_by = 30
    template_name = "ui/list/groups.html"


class GroupDetailView(generic.DetailView):
    """Displays a Group"""

    model = Group
    queryset = Group.objects.prefetch_related("pages")
    template_name = "ui/detail/group.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute page_list and add it to context"""

        return {
            **super().get_context_data(**kwargs),
            "prev_id": self.object.id - 1,
            "next_id": self.object.id + 1,
            "pages": Page.objects.filter(verses__group_id=self.object.id).distinct(),
        }


class QuarterListView(generic.ListView):
    """Displays all Quarters"""

    model = Quarter
    paginate_by = 60
    template_name = "ui/list/quarters.html"


class QuarterDetailView(generic.DetailView):
    """Displays a Quarter"""

    model = Quarter
    queryset = Quarter.objects.prefetch_related("pages")
    template_name = "ui/detail/quarter.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute page_list and add it to context"""

        return {
            **super().get_context_data(**kwargs),
            "prev_id": self.object.id - 1,
            "next_id": self.object.id + 1,
            "pages": Page.objects.filter(verses__quarter_id=self.object.id).distinct(),
        }


class PageListView(generic.ListView):
    """Displays all Pages"""

    model = Page
    paginate_by = 100
    template_name = "ui/list/pages.html"


class PageDetailView(generic.DetailView):
    """Displays a Page"""

    model = Page
    queryset = Page.objects.prefetch_related("verses")
    template_name = "ui/detail/Page.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute page_list and add it to context"""

        return {
            **super().get_context_data(**kwargs),
            "prev_id": self.object.id - 1,
            "next_id": self.object.id + 1,
            "pages": Page.objects.filter(verses__page_id=self.object.id).distinct(),
        }
