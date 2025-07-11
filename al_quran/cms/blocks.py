"""Custom blocks StreamField"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageBlock
from wagtailcodeblock.blocks import CodeBlock


# Create your blocks here.
class TextContentBlock(blocks.StreamBlock):
    """Custom StreamBlock for Text content"""

    quote = blocks.BlockQuoteBlock(help_text=_("Quote"))
    paragraph = blocks.RichTextBlock(help_text=_("Paragraph"))


class CommonContentBlock(TextContentBlock):
    """Custom StreamBlock for Text and Media content"""

    code = CodeBlock(help_text=_("Code"))
    image = ImageBlock(help_text=_("Image"))
    document = DocumentChooserBlock(help_text=_("Document"))
