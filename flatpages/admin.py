from __future__ import unicode_literals

from copy import deepcopy

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.admin import (DisplayableAdmin,
                                  BaseTranslationModelAdmin)
from mezzanine.twitter.admin import TweetableAdminMixin
from mezzanine.pages.admin import PageAdmin

from flatpages.models import FlatPage, FlatPageCategory, FlatPageIndex

class FlatPageAdmin(TweetableAdminMixin, DisplayableAdmin):
    fieldsets = [
        (None, {
            "fields":["title", "status", ("publish_date", "expiry_date"),"featured_image","content",]
        }),
         (_("Authors"), {
            'classes': ('collapse-closed',),
            'fields': ['authors',]
        }),
        (_("Categories"), {
            'classes': ('collapse-closed',),
            'fields': ['categories',]
        }),
        (_("Meta data"), {
            "fields":["_meta_title", "slug", ("description", "gen_description"), "keywords", "in_sitemap"], 
            "classes":("collapse-closed", )
        }),        
    ]
    
    list_display = ("admin_thumb","title", "status", "admin_link")
    list_filter = ("status", "keywords__keyword", "categories", "authors")
    filter_horizontal = ("categories","authors")


class FlatPageCategoryAdmin(BaseTranslationModelAdmin):
    """
    Admin class for blog categories. Hides itself from the admin menu
    unless explicitly specified.
    """

    fieldsets = ((None, {"fields": ("title","slug")}),)

    def has_module_permission(self, request):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "flatpages.FlatPageCategory" in items:
                return True
        return False

flatpageindex_extra_fieldsets = ((None, {"fields": ("category",)}),)   
class FlatPageIndexAdmin(PageAdmin):
    fieldsets = flatpageindex_extra_fieldsets + deepcopy(PageAdmin.fieldsets)


admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(FlatPageCategory, FlatPageCategoryAdmin)
admin.site.register(FlatPageIndex, FlatPageIndexAdmin)