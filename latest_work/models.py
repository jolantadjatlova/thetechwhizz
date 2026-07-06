from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class LatestWorkIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    class Meta:
        verbose_name = "Latest Work Index Page"


class LatestWorkPage(Page):
    CATEGORY_CHOICES = [
        ('wifi', 'Wi-Fi'),
        ('smart_home', 'Smart Home'),
        ('cctv', 'CCTV'),
        ('broadband', 'Home Broadband'),
        ('training', 'Training'),
        ('networking', 'Home Networking'),
        ('other', 'Other'),
    ]

    date = models.DateField("Post date")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='other'
    )
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
        ], heading="Post details"),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('main_image'),
    ]

    class Meta:
        verbose_name = "Latest Work Post"