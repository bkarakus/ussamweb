# encoding: utf-8

from django.db import models
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import NoReverseMatch
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from mezzanine.utils.urls import admin_url

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter


# Register your models here.
from portlets.models import (Portlet,
                             TextPortlet,
                             AnnouncementPortlet,
                             SlideShowPortlet,
                             DialogPortlet,
                             MenuPortlet,
                             PagePortlet)

class PortletChildAdmin(PolymorphicChildModelAdmin):
    base_model = Portlet

    # On purpose, only have the shared fields here.
    # The fields of the derived model should still be displayed.
    base_fieldsets = (
        ("Base fields", {
            'fields': ('title', 'slot', 'order',)
        }),
    )
    
@admin.register(TextPortlet)
class TextPorletAdmin(PortletChildAdmin):
    base_model = TextPortlet
    
    def has_module_permission(self, request):
        return False

    
@admin.register(AnnouncementPortlet)
class AnnouncementPortletAdmin(PortletChildAdmin):
    base_model = AnnouncementPortlet
    
    def has_module_permission(self, request):
        return False

    
@admin.register(Portlet)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Portlet
    child_models = (TextPortlet, AnnouncementPortlet)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.

'''
class PortletAdmin(admin.ModelAdmin):
    list_filter = ('slot', 'status')
    list_display = ('title','language', 'slot', 'order',)
    radio_fields = {'status': admin.HORIZONTAL}
    
        
    def _check_permission(self, request, page, permission):
        """
        Runs the custom permission check and raises an
        exception if False.
        """
        if not getattr(page, "can_" + permission)(request):
            raise PermissionDenied
        
    def change_view(self, request, object_id, **kwargs):
        """
        For the ``Page`` model, check ``page.get_content_model()``
        for a subclass and redirect to its admin change view.
        Also enforce custom change permissions for the page instance.
        """
        portlet = get_object_or_404(Portlet, pk=object_id)
        content_model = portlet.get_content_model()
        self._check_permission(request, content_model, "change")
        if self.model is Portlet:
            if content_model is not None:
                change_url = admin_url(content_model.__class__, "change",
                                       content_model.id)
                return HttpResponseRedirect(change_url)
        kwargs.setdefault("extra_context", {})
        kwargs["extra_context"].update({
            "hide_delete_link": not content_model.can_delete(request),
        })
        return super(PortletAdmin, self).change_view(request, object_id, **kwargs)
        
    def changelist_view(self, request, extra_context=None):
        """
        Redirect to the ``Page`` changelist view for ``Page``
        subclasses.
        """
        if self.model is not Portlet:
            return HttpResponseRedirect(admin_url(Portlet, "changelist"))
        if not extra_context:
            extra_context = {}
        extra_context["portlet_models"] = self.get_content_models()
        return super(PortletAdmin, self).changelist_view(request, extra_context)
    
    @classmethod
    def get_content_models(cls):
        """
        Return all Page subclasses that are admin registered, ordered
        based on the ``ADD_PAGE_ORDER`` setting.
        """
        models = []
        for model in Portlet.get_content_models():
            try:
                admin_url(model, "add")
            except NoReverseMatch:
                continue
            else:
                setattr(model, "meta_verbose_name", model._meta.verbose_name)
                setattr(model, "add_url", admin_url(model, "add"))
                models.append(model)

        def sort_key(page):
            name = "%s.%s" % (page._meta.app_label, page._meta.object_name)
        return sorted(models, key=sort_key)
    
    def hide_in_menu(self):
        return self.model is not Portlet
    
class TextPortletAdmin(PortletAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['slot', 'title' , 'status', 'kampus_ici', 'publish_date', 'expiry_date', 'content']
        }),
        (u'', {
            'classes': ('suit-tab suit-tab-show-options',),
            'fields': ['css_classes','header_css_classes', 'body_css_classes',]
        }),
            
    ]
    
    suit_form_tabs = (('general', 'General'),('show-options', u'Seçenekler'),)
    
class AnnouncementPortletAdmin(PortletAdmin):
    radio_fields = {'status': admin.HORIZONTAL, 'category': admin.HORIZONTAL}
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['slot', 'category', 'title' , 'status', 'kampus_ici', 'publish_date', 'expiry_date', 'count']
        }),
        (u'', {
            'classes': ('suit-tab suit-tab-show-options',),
            'fields': ['show_thumbnail', 'height', 'css_classes','header_css_classes', 'body_css_classes',]
        }),
            
    ]
    
    suit_form_tabs = (('general', 'General'),('show-options', u'Seçenekler'),)
    
class SlideShowPortletAdmin(PortletAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['slot', 'title', 'size', 'status', 'kampus_ici', 'publish_date', 'expiry_date',]
        }),
        (u'', {
            'classes': ('suit-tab suit-tab-show-options',),
            'fields': ['css_classes','header_css_classes', 'body_css_classes', 'captions', 'js_option']
        }),
        (u'NivoSlider Seçenekleri', {
            'classes': ('suit-tab suit-tab-show-options',),
            'fields': ['theme',]
        }),
        (u'BxSlider Seçenekleri', {
            'classes': ('suit-tab suit-tab-show-options',),
            'fields': ['mode', 'pager', 'auto', 'carouselMode', 'maxSlides', 'minSlides', 'slideWidth',]
        }),
            
    ]
    
    suit_form_tabs = (('general', 'General'),('show-options', u'Seçenekler'), ('images', 'Resimler'))
   
    suit_form_includes = (
        ('admin/files/images.html', 'middle', 'images'),
        ('admin/files/upload_image_button.html', 'middle', 'images'),
    )
    
class DialogPortletAdmin(PortletAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['title' , 'status', 'kampus_ici', 'publish_date', 'expiry_date', 'content']
        }),
        (u'', {
            'classes': ('suit-tab suit-tab-show-options',),
            'fields': ['width', 'timeout', 'css_classes','header_css_classes', 'body_css_classes',]
        }),
            
    ]
    
    suit_form_tabs = (('general', 'General'),('show-options', u'Seçenekler'),)
    
class MenuPortletAdmin(PortletAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['slot', 'title' , 'status', 'kampus_ici', 'publish_date', 'expiry_date', 'menu']
        }),
        (u'', {
            'classes': ('suit-tab suit-tab-show-options',),
            'fields': ['template','css_classes','header_css_classes', 'body_css_classes',]
        }),
            
    ]
    
    suit_form_tabs = (('general', 'General'),('show-options', u'Seçenekler'),)
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(MenuPortletAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'menu':
                field.queryset = field.queryset.filter(can_have_children=True)

        return field
    
class PagePortletAdmin(PortletAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['slot', 'title' , 'status', 'kampus_ici', 'publish_date', 'expiry_date', 'page']
        }),
        (u'', {
            'classes': ('suit-tab suit-tab-show-options',),
            'fields': ['css_classes','header_css_classes', 'body_css_classes',]
        }),
            
    ]
    
    suit_form_tabs = (('general', 'General'),('show-options', u'Seçenekler'),)
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(PagePortletAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'page':
                field.queryset = field.queryset.filter(content_model__in=['richtextpage', 'videopage',])

        return field
    
admin.site.register(Portlet, PortletAdmin)
admin.site.register(TextPortlet, TextPortletAdmin)
admin.site.register(AnnouncementPortlet, AnnouncementPortletAdmin)
admin.site.register(SlideShowPortlet, SlideShowPortletAdmin)
admin.site.register(DialogPortlet, DialogPortletAdmin)
admin.site.register(MenuPortlet, MenuPortletAdmin)
admin.site.register(PagePortlet, PagePortletAdmin)
'''
