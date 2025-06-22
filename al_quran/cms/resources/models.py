"""Data Models for al_quran.cms.resources"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index

from al_quran.cms.blocks import CommonContentBlock
from al_quran.cms.resources import RESOURCE_TYPES


# Create your models here.
class Resource(Page):
    """Quran data resource"""

    type = models.PositiveSmallIntegerField(
        help_text=_("Resource type"),
        choices=RESOURCE_TYPES,
    )
    description = RichTextField(help_text=_("Resource description"))
    content = StreamField(
        CommonContentBlock(),
        help_text=_("Blog content"),
    )
    tags = ClusterTaggableManager(
        blank=True,
        through="tags.PostTag",
        help_text=_("Resource tags"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Date created"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=_("Last update"),
    )

    # Dashboard UI config
    context_object_name = "resource"
    template = "cms/resource.html"
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("content"),
        FieldPanel("tags"),
    ]
    page_description = _("Quran resources")

    # Search fields
    search_fields = Page.search_fields + [
        index.SearchField("description"),
        index.SearchField("content"),
    ]

    # API fields
    api_fields = [APIField("description"), APIField("content"), APIField("tags")]

    def __str__(self) -> str:
        return self.title
