from django.conf import settings

from mezzanine.core.admin import StackedDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
#from mezzanine.forms.admin import FormAdmin
from mezzanine.galleries.admin import GalleryAdmin

from .models import Slide


class SlideInline(StackedDynamicInlineAdmin):
    model = Slide

admin_classes_with_slides = [PageAdmin, GalleryAdmin]

for admin_class in admin_classes_with_slides:
    setattr(admin_class, 'inlines', list(admin_class.inlines) + [SlideInline])