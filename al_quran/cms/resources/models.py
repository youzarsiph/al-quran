"""Data Models for al_quran.cms.resources"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index

from al_quran.cms.blocks import CommonContentBlock
from al_quran.cms.resources import RESOURCE_TYPES
from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class Resource(DateTimeMixin, Page):
    """Quran data resource"""

    type = models.CharField(
        max_length=32,
        choices=RESOURCE_TYPES,
        verbose_name=_("type"),
        help_text=_("Resource type"),
    )
    description = RichTextField(
        verbose_name=_("description"),
        help_text=_("Resource description"),
    )
    content = StreamField(
        CommonContentBlock(),
        verbose_name=_("content"),
        help_text=_("Resource content"),
    )

    # Dashboard UI config
    context_object_name = "resource"
    template = "cms/resources/resource.html"
    content_panels = Page.content_panels + [
        FieldPanel("type"),
        FieldPanel("description"),
        FieldPanel("content"),
    ]
    page_description = _("Quran resources")

    # Search fields
    search_fields = Page.search_fields + [
        index.FilterField("type"),
        index.SearchField("description"),
        index.SearchField("content"),
    ]

    parent_page_types = ["page.ResourcesHome"]

    # API fields
    api_fields = [
        APIField("type"),
        APIField("description"),
        APIField("content"),
    ]

    def __str__(self) -> str:
        return self.title
