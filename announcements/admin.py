from __future__ import unicode_literals

from copy import deepcopy

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.admin import (DisplayableAdmin,
                                  BaseTranslationModelAdmin)
from mezzanine.twitter.admin import TweetableAdminMixin

from announcements.models import Announcement, AnnouncementCategory

announcement_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
announcement_fieldsets[0][1]["fields"].insert(1, "categories")
announcement_fieldsets[0][1]["fields"].extend(["content",])
announcement_list_display = ["title", "status", "admin_link"]
announcement_fieldsets[0][1]["fields"].insert(-2, "featured_image")
announcement_list_display.insert(0, "admin_thumb")
announcement_fieldsets = list(announcement_fieldsets)
announcement_list_filter = deepcopy(DisplayableAdmin.list_filter) + ("categories",)


class AnnouncementAdmin(TweetableAdminMixin, DisplayableAdmin):
    """
    Admin class for blog posts.
    """

    fieldsets = announcement_fieldsets
    list_display = announcement_list_display
    list_filter = announcement_list_filter
    filter_horizontal = ("categories",)


class AnnouncementCategoryAdmin(BaseTranslationModelAdmin):
    """
    Admin class for blog categories. Hides itself from the admin menu
    unless explicitly specified.
    """

    fieldsets = ((None, {"fields": ("title",)}),)

    def has_module_permission(self, request):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "announcement.AnnouncementCategory" in items:
                return True
        return False


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(AnnouncementCategory, AnnouncementCategoryAdmin)