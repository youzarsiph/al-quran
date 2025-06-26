"""Data Models for al_quran.cms.page"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from al_quran.cms.blocks import CommonContentBlock
from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class BaseHome(DateTimeMixin, models.Model):
    """Base home page"""

    content = StreamField(
        CommonContentBlock(),
        verbose_name=_("content"),
        help_text=_("Home page content"),
    )

    # Dashboard UI
    content_panels = Page.content_panels + [FieldPanel("content")]

    # Search fields
    search_fields = Page.search_fields + [index.SearchField("content")]

    # API fields
    api_fields = [APIField("content"), APIField("created_at"), APIField("updated_at")]

    def __str__(self) -> str:
        return self.title

    class Meta:
        """Meta data"""

        abstract = True


class BlogHome(BaseHome, Page):
    """Blog home page"""

    template = "cms/blog/home.html"
    page_description = _("Blog home page")
    parent_page_type = []
    subpage_types = ["blog.Post"]


class ResourcesHome(BaseHome, Page):
    """Resources home page"""

    template = "cms/resources/home.html"
    page_description = _("Quran Resources home page")
    parent_page_type = []
    subpage_types = ["resources.Resource"]
