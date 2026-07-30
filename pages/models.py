from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey

from .forms import ContactForm


class AboutPage(Page):
    body = RichTextField(blank=True)
    about_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('about_image'),
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
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel("anchor_id"),
        FieldPanel("title"),
        FieldPanel("body"),
        FieldPanel("image"),
    ]


class ContactPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Contact Page"

    def serve(self, request, *args, **kwargs):
        form = ContactForm()

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                messages.success(request, "Thanks for your message! We'll be in touch soon.")
                return redirect(self.url)

        context = self.get_context(request)
        context['form'] = form
        return render(request, self.get_template(request), context)


class PrivacyPolicyPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Privacy Policy Page"