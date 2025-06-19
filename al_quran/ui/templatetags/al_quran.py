"""Custom template tags for Al Quran"""

from typing import Optional

from django import template

from al_quran.comp.collections.models import Collection

register = template.Library()


# Create your template tags here.
@register.simple_tag
def get_verse_item(collection_id: Optional[int], verse_id: Optional[int]) -> str:

    if collection_id and verse_id:
        return (
            Collection.objects.get(pk=collection_id)
            .items.get(verse_id=verse_id)
            .content
        )

    return ""
