"""A model to use a `through` model to define relation between models and tags"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


# Create your models here.
class PostTag(TaggedItemBase):
    """Through model for defining m2m rel between Posts and Tags"""

    content_object = ParentalKey(
        "blog.Post",
        on_delete=models.CASCADE,
        related_name="tagged_posts",
        verbose_name=_("tags"),
        help_text=_("Tags"),
    )


class ResourceTag(TaggedItemBase):
    """Through model for defining m2m rel between Resources and Tags"""

    content_object = ParentalKey(
        "resources.Resource",
        on_delete=models.CASCADE,
        related_name="tagged_resources",
        verbose_name=_("tags"),
        help_text=_("Tags"),
    )
