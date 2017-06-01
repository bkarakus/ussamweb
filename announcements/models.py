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


class Announcement(Displayable, RichText, AdminThumbMixin):
    """
    A blog post.
    """

    categories = models.ManyToManyField("AnnouncementCategory",
                                        verbose_name=_("Categories"),
                                        blank=True, related_name="announcements")
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("announcements.Announcement.featured_image", "announcements"),
        format="Image", max_length=255, null=True, blank=True)

    admin_thumb_field = "featured_image"

    class Meta:
        verbose_name = _("Duyuru")
        verbose_name_plural = _("Duyurular")
        ordering = ("-publish_date",)

    @models.permalink
    def get_absolute_url(self):
        return ('home', (), {})
        #return ("/", (), {"slug": self.slug})

class AnnouncementCategory(Slugged):
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
    