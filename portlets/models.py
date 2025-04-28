# encoding: utf-8
import json

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

from polymorphic.models import PolymorphicModel
from polymorphic.managers import PolymorphicManager

from mezzanine.core.models import Displayable, RichText, ContentTyped, Slugged
from mezzanine.core.managers import DisplayableManager
from mezzanine.core.fields import FileField
from mezzanine.pages.models import Page
from mezzanine.utils.sites import current_request

from slides.models import Slide

PORTLET_SLOTS = (
    ('ana-sayfa',_(u'Ana Sayfa')),
    ('sag', _(u'Sağ')),
    ('sol', _(u'Sol')),
    ('alt', _(u'Alt')),
    ('menu-alti', _(u'Menu Altı')),
    ('menu-ustu', _(u'Menu Üstü')),
)

class PortletManager(PolymorphicManager, DisplayableManager):
    pass

class Portlet(PolymorphicModel, Displayable):
    slot = models.CharField(u"Yer", max_length=10, choices=PORTLET_SLOTS)
    order = models.PositiveSmallIntegerField(u"Sıra", default=999)
    css_classes = models.CharField(blank=True, max_length=100, default='col-md-12')
    header_css_classes = models.CharField(blank=True, max_length=100, help_text=u'Başlığı gizlemek için hidden ekleyiniz')
    body_css_classes = models.CharField(blank=True, max_length=100)
    
    class Meta:
        verbose_name = u"modül"
        verbose_name_plural = u"modüller"
        ordering = ('order',)
        
    objects = PortletManager()
        
    def can_add(self, request):
        """
        Dynamic ``add`` permission for content types to override.
        """
        return True

    def can_change(self, request):
        """
        Dynamic ``change`` permission for content types to override.
        """
        return True

    def can_delete(self, request):
        """
        Dynamic ``delete`` permission for content types to override.
        """
        return True

    def get_absolute_url(self):
        return ""


    def render(self):
        return None

class TextPortlet(Portlet, RichText):
    class Meta:
        verbose_name = u"Metin Modülü"
        verbose_name_plural = u"Metin Modülleri"
        
    def render(self, context):
        """
        Return the portlet as html
        """
        return render_to_string("portlets/text_portlet.html", {
            "title":self.title,
            "css_classes":self.css_classes,
            "header_css_classes":self.header_css_classes,
            "body_css_classes":self.body_css_classes,
            "text":self.content,
        })
        
class CategoryPortlet(Portlet):
    DEFAULT_TEMPLATE = 'portlets/category.html'
    NEWS_TEMPLATE = 'portlets/category_news.html'
    VERTICAL_TEMPLATE = 'portlets/category_vertical.html'
    SIDEBAR_TEMPLATE = 'portlets/category_sidebar.html'
    
    TEMPLATES = (
        (DEFAULT_TEMPLATE, u'Ön Tanımlı'),
        (NEWS_TEMPLATE, u'Haberler'),
        (VERTICAL_TEMPLATE, u'Yukarı Doğru Kayan'),
        (SIDEBAR_TEMPLATE, u'Sidebar'),
    )
    
    category = models.ForeignKey("flatpages.FlatPageCAtegory")
    count = models.PositiveSmallIntegerField(u'Sayı', default=10, help_text=u"Gösterilecek sayfa sayısı")
    width = models.PositiveSmallIntegerField(u'Resim Genişliği', default=0)
    height = models.PositiveSmallIntegerField(u'Resim Yüksekliği', default=0)
    
    template = models.CharField(u'Tema Dosyası', max_length=100, blank=True, null=True, default=DEFAULT_TEMPLATE, choices=TEMPLATES)
    
    class Meta:
        verbose_name = u"Kategori Modülü"
        verbose_name_plural = u"Kategori Modülleri"
        
    def render(self, context):
        """
        Return the portlet as html
        """
        flatpages_list = self.category.flatpages.all()[:self.count]
        return render_to_string(self.template, {
            "category": self.category,
            "title":self.title,
            "css_classes":self.css_classes,
            "header_css_classes":self.header_css_classes,
            "body_css_classes":self.body_css_classes,
            "flatpages_list": flatpages_list,
            "width": self.width,
            "height": self.height
        })
        
class SlideShowPortlet(Portlet):
    DEFAULT_TEMPLATE = 'portlets/slideshow.html'
    
    TEMPLATES = (
        (DEFAULT_TEMPLATE, u'Ön Tanımlı'),
    )
    
    template = models.CharField(u'Tema Dosyası', max_length=100, blank=True, null=True, default=DEFAULT_TEMPLATE, choices=TEMPLATES)
    count = models.PositiveSmallIntegerField(u'Sayı', default=10, help_text=u"Gösterilecek slide sayısı")
    width = models.PositiveSmallIntegerField(u'Resim Genişliği', default=0)
    height = models.PositiveSmallIntegerField(u'Resim Yüksekliği', default=0)
    
    class Meta:
        verbose_name = u"Slideshow Modülü"
        verbose_name_plural = u"Slideshow Modülleri"
        
    def render(self, context):
        """
        Return the portlet as html
        """
        slides = Slide.objects.published()
        slides = slides.filter(show_on_homepage=True)[:self.count]
        return render_to_string(self.template, {
            "id": self.pk,                       
            "title":self.title,
            "slides": slides,
            "css_classes":self.css_classes,
            "header_css_classes":self.header_css_classes,
            "body_css_classes":self.body_css_classes,
            "width": self.width,
            "height": self.height
        })
