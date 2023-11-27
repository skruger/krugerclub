
from wagtail.models import Page
from wagtail import fields
from wagtail.admin.panels import FieldPanel

from wtknowledgebase.blocks import stream_builder


class HomePage(Page):
    subpage_types = [
        'blog.BlogIndexPage',
        'krugercms.GenericPage',
        'wtknowledgebase.KbIndexPage',
    ]

    body = fields.StreamField(stream_builder.blocks([]), use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class GenericPage(Page):
    body = fields.StreamField(stream_builder.blocks([]), use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
