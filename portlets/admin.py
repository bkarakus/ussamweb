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
                             TextPortlet)

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
    
@admin.register(Portlet)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Portlet
    child_models = (TextPortlet, )
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.