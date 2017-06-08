from __future__ import unicode_literals

from copy import deepcopy

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.admin import (DisplayableAdmin,
                                  BaseTranslationModelAdmin)
from mezzanine.twitter.admin import TweetableAdminMixin
from mezzanine.pages.admin import PageAdmin

from flatpages.models import FlatPage, FlatPageCategory, FlatPageIndex

flatpages_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
flatpages_fieldsets[0][1]["fields"].insert(1, "categories")
flatpages_fieldsets[0][1]["fields"].extend(["content",])
flatpages_list_display = ["title", "status", "admin_link"]
flatpages_fieldsets[0][1]["fields"].insert(-2, "featured_image")
flatpages_list_display.insert(0, "admin_thumb")
flatpages_fieldsets = list(flatpages_fieldsets)
flatpages_list_filter = deepcopy(DisplayableAdmin.list_filter) + ("categories",)

flatpageindex_extra_fieldsets = ((None, {"fields": ("category",)}),)


class FlatPageAdmin(TweetableAdminMixin, DisplayableAdmin):
    """
    Admin class for blog posts.
    """

    fieldsets = flatpages_fieldsets
    list_display = flatpages_list_display
    list_filter = flatpages_list_filter
    filter_horizontal = ("categories",)


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
    
class FlatPageIndexAdmin(PageAdmin):
    fieldsets = flatpageindex_extra_fieldsets + deepcopy(PageAdmin.fieldsets)


admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(FlatPageCategory, FlatPageCategoryAdmin)
admin.site.register(FlatPageIndex, FlatPageIndexAdmin)