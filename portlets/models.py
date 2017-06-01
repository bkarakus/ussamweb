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

from mezzanine.core.models import Displayable, LanguageRelated, RichText, ContentTyped, Slugged
from mezzanine.core.managers import DisplayableManager
from mezzanine.core.fields import FileField
from mezzanine.pages.models import Page
from mezzanine.utils.sites import current_request

from announcements.models import Announcement, AnnouncementCategory

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
        
class AnnouncementPortlet(Portlet):
    category = models.ForeignKey(AnnouncementCategory, verbose_name=u'kategori', blank=True, null=True,)
    show_thumbnail = models.BooleanField(u'Resimleri Göster', default=False)
    count = models.IntegerField(u"sayı", default=10)
    height = models.PositiveSmallIntegerField(u'Yükseklik', default=250)
    
    class Meta:
        verbose_name = u"Duyuru Modülü"
        verbose_name_plural = u"Duyuru Modülleri"
        
    def render(self, context):
        qs = Announcement.objects.published()
        url = reverse('tum_duyuru_list')
        if self.category:
            qs = qs.filter(category=self.category)
        return render_to_string("portlets/news_portlet.html", {
            "title":self.title,
            "css_classes":self.css_classes,
            "header_css_classes":self.header_css_classes,
            "body_css_classes":self.body_css_classes,
            "news": qs[:self.count],
            "show_thumbnail": self.show_thumbnail,
            "url_tumu": url,
            "height": self.height,
        })
    
    
class SlideShowPortlet(Portlet):
    SIZES = (
        ('big', _(u'800x0')),
        ('normal', _(u'500x0')),
        ('billboard-l', _(u'950x250 - Resim merkezden kırpılır.')),
        ('billboard-m', _(u'700x300 - Resim merkezden kırpılır.')),
        ('billboard-mm', _(u'700x319 - Resim merkezden kırpılır.')),
        ('billboard-s', _(u'400x300 - Resim merkezden kırpılır.')),
        ('billboard-xs', _(u'250x354 - Afişler için bu seçeneği kullanınız.')),
        ('small-xs', _(u'150x50')),
    )
    THEMES = (
        ('theme-default', 'Default'),
        ('theme-light', 'Açık Tema 1'),
        ('theme-light2', 'Açık Tema 2'),
        ('theme-dark', 'Koyu Tema 1'),
    )
    
    SLIDER_JS_OPTIONS = (
        ('nivoSlider', 'Nivo Slider'),
        ('bxslider', 'BxSlider'),
        ('bs-carousel', 'Boostrap Carousel')
    )
    
    MODES = (
        ('horizontal', 'horizontal (yatay)'),
        ('vertical', 'vertical (dikey)'),
        ('fade', 'fade')
    )
    
    size = models.CharField(u"Boyut",max_length=30, choices=SIZES, blank=True, null=True)
    js_option = models.CharField(u"Kullanılacak Javascript Kütüphanesi", max_length=15, choices=SLIDER_JS_OPTIONS,
                                 blank=True, null=True,
                                 help_text=u"Kullanmak istediğiniz javascript kütüphanesini seçtikten sonra ilgili kütüphanenin seçeneklerini düzenleyiniz")
    theme = models.CharField(u"Tema", max_length=30, choices=THEMES, blank=True, null=True)
    mode = models.CharField(u"Mod", max_length=10, choices=MODES, blank=True, null=True)
    pager = models.BooleanField(u'Sayfalayıcı', default=False)
    auto = models.BooleanField(u'Auto Start', default=True)
    captions = models.BooleanField(u'Resim Başlıklarını Göster', default=True)
    carouselMode = models.BooleanField(u"Bir slide'de birden fazla resim olsun", default=False)
    maxSlides = models.PositiveSmallIntegerField(u"Maksimum Slide sayısı", default=3, )
    minSlides = models.PositiveSmallIntegerField(u"Minimum Slide Sayısı(küçük ekranlar için)", default=2)
    slideWidth = models.PositiveSmallIntegerField(u"Slide genişliği", default=315)
    moveSlides = models.PositiveSmallIntegerField(default=1, editable=False)
    
    class Meta:
        verbose_name = u"Slideshow Modülü"
        verbose_name_plural = u"slideshow modülleri"
        
    def get_templatenames(self):
        if self.js_option:
            template = 'portlets/slideshow_%s_portlet.html' % (self.js_option)
        else:
            template = 'portlets/slideshow_portlet.html'
            
        return [template, 'portlets/slideshow_portlet.html',]
        
    def render(self, context):
        return render_to_string(self.get_templatenames(), {
            "object": self,
            "css_classes": self.css_classes,
            "header_css_classes": self.header_css_classes,
            "body_css_classes": self.body_css_classes,
            "images": self.images.all(),
            "size": self.size,
            "theme": self.theme,
            "id": self.pk,
        })
        
class DialogPortlet(Portlet, RichText):
    width = models.PositiveIntegerField(u'Genişlik', default=400)
    timeout = models.PositiveIntegerField(u'Zaman Aşımı', default=30,
            help_text=u"Mesaj bir defa gösterildikten kaç dakika sonra tekrar gösterilsin?")
    
    class Meta:
        verbose_name = u"dialog modülü"
        verbose_name_plural = u"dialog modülleri"
        
    def save(self, *args, **kwargs):
        self.slot = 'modal'
        super(DialogPortlet, self).save(args, kwargs)
    
    def render(self, context):
        html = render_to_string("portlets/dialog_portlet.html", {
            "title":self.title,
            "css_classes":self.css_classes,
            "header_css_classes":self.header_css_classes,
            "body_css_classes":self.body_css_classes,
            "text":self.rendered_content,
            "width": self.width,
        })
        return html
    
class MenuPortlet(Portlet):
    DEFAULT_TEMPLATE = 'portlets/menu_portlet.html'
    SMALL_ICON_TEMPLATE = 'portlets/menu_portlet_small.html'
    ALT_MENU_TEMPLATE = 'portlets/menu_portlet_alt.html'
    BOX_MENU_TEMPLATE = 'portlets/menu_portlet_box.html'
    
    MENUTEMPLATES = (
        (DEFAULT_TEMPLATE, u'Ön Tanımlı'),
        (SMALL_ICON_TEMPLATE, u'Küçük İkon'),
        (ALT_MENU_TEMPLATE, u'Alt Menu'),
        (BOX_MENU_TEMPLATE, u'Resimli Kutu')
    )
    
    menu = models.ForeignKey(Page, verbose_name=u'Menü')
    template = models.CharField('Tema dosyası', max_length=100, choices=MENUTEMPLATES,blank=True, null=True)
    
    class Meta:
        verbose_name = u"menü modülü"
        verbose_name_plural = u"menü modülleri"
        
    def render(self, context):
        """
        Return the portlet as html
        """
        if not self.template:
            self.template = MenuPortlet.DEFAULT_TEMPLATE
        
        html = render_to_string(self.template, {
            "title":self.title,
            "css_classes":self.css_classes,
            "header_css_classes":self.header_css_classes,
            "body_css_classes":self.body_css_classes,
            "menu": self.menu,
            "portlet": self,
        })
        
        return html
    
class PagePortlet(Portlet):
    page = models.ForeignKey(Page, verbose_name=u'Sayfa')
    
    class Meta:
        verbose_name = u"sayfa modülü"
        verbose_name_plural = u"sayfa modülleri"
    
    def render(self, context):
        self.template = 'portlets/%s_portlet.html' % self.page.content_model
        
        self.page = self.page.get_content_model()
        
        html = render_to_string(self.template, {
            "title":self.title,
            "css_classes":self.css_classes,
            "header_css_classes":self.header_css_classes,
            "body_css_classes":self.body_css_classes,
            "page": self.page,
        })
        
        return html