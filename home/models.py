from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey


class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('testimonials', label="Testimonials"),
    ]

    @property
    def testimonial_groups(self):
        items = list(self.testimonials.all())
        return [items[i:i+3] for i in range(0, len(items), 3)]


class Testimonial(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="testimonials")
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)

    panels = [
        FieldPanel("name"),
        FieldPanel("location"),
        FieldPanel("quote"),
        FieldPanel("rating"),
    ]