# encoding: utf-8
from __future__ import unicode_literals
from future.builtins import str

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Ownable, RichText, Slugged
from mezzanine.generic.fields import CommentsField, RatingField
from mezzanine.utils.models import AdminThumbMixin, upload_to
from mezzanine.pages.models import Page

class FlatPage(Displayable, RichText, AdminThumbMixin):
    """
    A blog post.
    """

    categories = models.ManyToManyField("FlatPageCategory",
                                        verbose_name=_("Categories"),
                                        blank=True, related_name="flatpages")
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("flatpages.FlatPage.featured_image", "flatpages"),
        format="Image", max_length=255, null=True, blank=True)

    admin_thumb_field = "featured_image"

    class Meta:
        verbose_name = _(u"Düz Sayfa")
        verbose_name_plural = _(u"Düz Sayfalar")
        ordering = ("-publish_date",)

    @models.permalink
    def get_absolute_url(self):
        return ('home', (), {})
        #return ("/", (), {"slug": self.slug})

class FlatPageCategory(Slugged):
    """
    A category for grouping blog posts into a series.
    """

    class Meta:
        verbose_name = _("Kategori")
        verbose_name_plural = _("Kategoriler")
        ordering = ("title",)
    
    @models.permalink
    def get_absolute_url(self):
        return ("/", (), {"category": self.slug})
    
class FlatPageIndex(Page):
    category = models.ForeignKey(FlatPageCategory)
    
    class Meta:
        verbose_name = _("Kategori Index")
        verbose_name_plural = _("Kategori Index Sayfaları")
    