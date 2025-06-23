"""Data Models for al_quran.cms.page"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from al_quran.cms.blocks import CommonContentBlock


# Create your models here.
class BaseHome(models.Model):
    """Base home page"""

    content = StreamField(
        CommonContentBlock(),
        help_text=_("Home page content"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Date created"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=_("Last update"),
    )

    # Dashboard UI
    content_panels = Page.content_panels + [FieldPanel("content")]

    # Search fields
    search_fields = Page.search_fields + [index.SearchField("content")]

    # API fields
    api_fields = [APIField("content"), APIField("created_at"), APIField("updated_at")]

    parent_page_type = ["wagtailcore.Page"]

    def __str__(self) -> str:
        return self.title

    class Meta:
        """Meta data"""

        abstract = True


class BlogHome(BaseHome, Page):
    """Blog home page"""

    template = "cms/blog/home.html"
    page_description = _("Blog home page")
    subpage_types = ["blog.Post"]


class ResourcesHome(BaseHome, Page):
    """Resources home page"""

    template = "cms/blog/home.html"
    page_description = _("Quran Resources home page")
    subpage_types = ["resources.Resource"]
