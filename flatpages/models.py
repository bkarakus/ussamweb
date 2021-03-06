# encoding: utf-8
from __future__ import unicode_literals
from future.builtins import str

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Ownable, RichText, Slugged
from mezzanine.generic.fields import CommentsField, RatingField
from mezzanine.utils.models import AdminThumbMixin, upload_to, get_user_model_name
from mezzanine.pages.models import Page

from .meta import LocalizeModelBase, Translate
from slides.models import Slide

user_model_name = get_user_model_name()

class FlatPage(Displayable, RichText, AdminThumbMixin):
    """
    A blog post.
    """

    categories = models.ManyToManyField("FlatPageCategory",
                                        verbose_name=_("Kategoriler"),
                                        blank=True, related_name="flatpages")
    authors = models.ManyToManyField(user_model_name, verbose_name=_("Yazarlar"), blank=True, related_name="flatpages")
    featured_image = FileField(verbose_name=_("Resim"),
        upload_to=upload_to("flatpages.FlatPage.featured_image", "flatpages"),
        format="Image", max_length=255, null=True, blank=True)

    admin_thumb_field = "featured_image"
    
    images = GenericRelation(Slide)

    class Meta:
        verbose_name = _(u"Düz Sayfa")
        verbose_name_plural = _(u"Düz Sayfalar")
        ordering = ("-publish_date",)

    @models.permalink
    def get_absolute_url(self):
        return ("flatpage_detail", (), {"slug": self.slug})

class FlatPageCategory(Slugged):
    __metaclass__ = LocalizeModelBase
    
    baslik_tr = models.CharField(_("Title [TR]"), max_length=500)
    baslik_en = models.CharField(_("Title [EN]"), max_length=500, blank=True, null=True)
    baslik_ar = models.CharField(_("Title [AR]"), max_length=500, blank=True, null=True)
    baslik = Translate

    class Meta:
        verbose_name = _("Kategori")
        verbose_name_plural = _("Kategoriler")
        ordering = ("title",)
        
    def __unicode__(self):
        return self.baslik
        
    def save(self, *args, **kwargs):
        self.title = self.baslik_tr
        super(FlatPageCategory, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ("flatpage_list_category", (), {"category": self.slug})
    
class FlatPageIndex(Page):
    category = models.ForeignKey(FlatPageCategory)
    
    class Meta:
        verbose_name = _("Kategori Index")
        verbose_name_plural = _("Kategori Index Sayfaları")
        
    def save(self, *args, **kwargs):
        slug = reverse("flatpage_list_category", kwargs={"category": self.category.slug})
        slug_parts = slug.strip('/').split('/')[1:]
        self.slug = '/'.join(slug_parts)
        super(FlatPageIndex, self).save(*args, **kwargs)
    