"""API endpoints for al_quran.ui"""

from typing import Any, Dict
from django.views import generic

from al_quran.core.chapters.models import Chapter
from al_quran.core.groups.models import Group
from al_quran.core.pages.models import Page
from al_quran.core.parts.models import Part
from al_quran.core.quarters.models import Quarter
from al_quran.ui.mixins import ExtraContextMixin


# Create your views here.
class HomeView(generic.TemplateView):
    """Home page"""

    template_name = "ui/index.html"


class AboutView(generic.TemplateView):
    """About page"""

    template_name = "ui/about.html"


class ChapterListView(generic.ListView):
    """Displays all Chapters"""

    model = Chapter
    paginate_by = 25
    template_name = "ui/list/chapters.html"


class ChapterDetailView(ExtraContextMixin, generic.DetailView):
    """Displays a Chapter"""

    model = Chapter
    queryset = Chapter.objects.prefetch_related("pages")
    template_name = "ui/detail/chapter.html"
    extra_context = {
        "template_name": "ui/list/chapters.html",
        "chapter_list": Chapter.objects.all(),
    }

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


class PartDetailView(ExtraContextMixin, generic.DetailView):
    """Displays a Part"""

    model = Part
    queryset = Part.objects.prefetch_related("pages")
    template_name = "ui/detail/part.html"
    extra_context = {
        "template_name": "ui/list/parts.html",
        "part_list": Part.objects.all(),
    }

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


class GroupDetailView(ExtraContextMixin, generic.DetailView):
    """Displays a Group"""

    model = Group
    queryset = Group.objects.prefetch_related("pages")
    template_name = "ui/detail/group.html"
    extra_context = {
        "template_name": "ui/list/groups.html",
        "group_list": Group.objects.all(),
    }

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


class QuarterDetailView(ExtraContextMixin, generic.DetailView):
    """Displays a Quarter"""

    model = Quarter
    queryset = Quarter.objects.prefetch_related("pages")
    template_name = "ui/detail/quarter.html"
    extra_context = {
        "template_name": "ui/list/quarters.html",
        "quarter_list": Quarter.objects.all(),
    }

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Compute page_list and add it to context"""

        return {
            **super().get_context_data(**kwargs),
            "prev_id": self.object.id - 1,
            "next_id": self.object.id + 1,
            "pages": Page.objects.filter(verses__quarter_id=self.object.id).distinct(),
        }
