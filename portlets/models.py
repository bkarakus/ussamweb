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

from mezzanine.core.models import Displayable, RichText, ContentTyped, Slugged
from mezzanine.core.managers import DisplayableManager
from mezzanine.core.fields import FileField
from mezzanine.pages.models import Page
from mezzanine.utils.sites import current_request

PORTLET_SLOTS = (
    ('ana-sayfa',_(u'Ana Sayfa')),
    ('sag', _(u'Sağ')),
    ('sol', _(u'Sol')),
    ('alt', _(u'Alt')),
    ('menu-alti', _(u'Menu Altı')),
    ('menu-ustu', _(u'Menu Üstü')),
)

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
        
    #objects = DisplayableManager()
        
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
            "text":self.rendered_content,
        })