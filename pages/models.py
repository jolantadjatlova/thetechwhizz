from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey


class AboutPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "About Page"


class ServicesPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('service_details', label="Services"),
    ]

    class Meta:
        verbose_name = "Services Page"


class ServiceDetail(Orderable):
    page = ParentalKey(ServicesPage, on_delete=models.CASCADE, related_name="service_details")
    anchor_id = models.SlugField(max_length=50, help_text="Short code, e.g. 'wifi' — no spaces")
    title = models.CharField(max_length=100)
    body = RichTextField()

    panels = [
        FieldPanel("anchor_id"),
        FieldPanel("title"),
        FieldPanel("body"),
    ]


class TestimonialsPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Testimonials Page"


class ContactPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Contact Page"