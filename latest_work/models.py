from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class LatestWorkIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['latestwork_categories'] = LatestWorkPage.CATEGORY_CHOICES
        return context

    class Meta:
        verbose_name = "Latest Work Index Page"


class LatestWorkPage(Page):
    CATEGORY_CHOICES = [
        ('it-help', 'Computer & IT Help'),
        ('wifi-internet', 'Wi-Fi & Internet Problems'),
        ('broadband-voice', 'Broadband & Digital Voice Setup'),
        ('device-setup', 'New PC, Laptop & Device Setup'),
        ('printer-support', 'Printer Setup & Support'),
        ('smart-home-security', 'Smart Home & Security'),
        ('tech-advice-supply', 'Tech Advice, Supply & Training'),
    ]

    date = models.DateField("Post date")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='it-help'
    )
    location = models.CharField(max_length=100, blank=True)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('category'),
            FieldPanel('location'),
        ], heading="Post details"),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('main_image'),
    ]

    class Meta:
        verbose_name = "Latest Work Post"