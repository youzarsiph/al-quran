"""Data Models for al_quran.cms.blog"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from al_quran.cms.blocks import CommonContentBlock
from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class Post(DateTimeMixin, Page):
    """Blog posts"""

    headline = models.CharField(
        max_length=128,
        db_index=True,
        verbose_name=_("headline"),
        help_text=_("Blog headline"),
    )
    content = StreamField(
        CommonContentBlock(),
        verbose_name=_("content"),
        help_text=_("Blog content"),
    )
    tags = ClusterTaggableManager(
        blank=True,
        through="tags.PostTag",
        verbose_name=_("tags"),
        help_text=_("Post tags"),
    )

    # Dashboard UI config
    context_object_name = "post"
    template = "cms/blog/post.html"
    content_panels = Page.content_panels + [
        FieldPanel("headline"),
        FieldPanel("content"),
        FieldPanel("tags"),
    ]
    page_description = _("Blog post")

    # Search fields
    search_fields = Page.search_fields + [
        index.SearchField("headline"),
        index.SearchField("content"),
    ]

    parent_page_types = ["page.BlogHome"]

    # API fields
    api_fields = [APIField("headline"), APIField("content"), APIField("tags")]

    def __str__(self) -> str:
        return self.title
