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
from portlets.models import (Portlet, TextPortlet,
                             CategoryPortlet, SlideShowPortlet)

class PortletChildAdmin(PolymorphicChildModelAdmin):
    base_model = Portlet

    # On purpose, only have the shared fields here.
    # The fields of the derived model should still be displayed.
    base_fieldsets = (
        ("Base fields", {
            'fields': ('title', 'slot', 'order','css_classes', 'header_css_classes', 'body_css_classes')
        }),
        ("Publish Info", {
            'fields': ('status', 'publish_date', 'expiry_date',)
        }),
    )
    
@admin.register(TextPortlet)
class TextPorletAdmin(PortletChildAdmin):
    base_model = TextPortlet
    
    def has_module_permission(self, request):
        return False
    
    def get_subclass_fields(self, request, obj=None):
        return ('content',)
    
@admin.register(CategoryPortlet)
class CategoryPorletAdmin(PortletChildAdmin):
    base_model = CategoryPortlet
    
    def get_subclass_fields(self, request, obj=None):
        return ('category', 'count', 'template', 'width', 'height')
    
    def has_module_permission(self, request):
        return False
    
@admin.register(SlideShowPortlet)
class SlideShowPorletAdmin(PortletChildAdmin):
    base_model = SlideShowPortlet
    
    def get_subclass_fields(self, request, obj=None):
        return ('template', 'count', 'width', 'height')
    
    def has_module_permission(self, request):
        return False
    
@admin.register(Portlet)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Portlet
    child_models = (TextPortlet, CategoryPortlet, SlideShowPortlet)
    list_filter = (PolymorphicChildModelFilter,'slot')  # This is optional.
    list_display = ('title', 'slot', 'order',)
    list_editable = ('order',)