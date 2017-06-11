from django.conf import settings
from django.contrib.contenttypes.admin import GenericStackedInline
from django.contrib import admin

from mezzanine.core.admin import StackedDynamicInlineAdmin, BaseTranslationModelAdmin
from mezzanine.pages.admin import PageAdmin
#from mezzanine.forms.admin import FormAdmin
from mezzanine.galleries.admin import GalleryAdmin

from flatpages.admin import FlatPageAdmin

from .models import Slide
from .forms import AlwaysChangedModelForm

class SlideAdmin(BaseTranslationModelAdmin):
    list_display = ("admin_thumb", "description", "caption")

class SlideInline(StackedDynamicInlineAdmin, GenericStackedInline):
    model = Slide
    form = AlwaysChangedModelForm
    readonly_fields = ('status', 'publish_date', 'expiry_date')
    max_num = 1

admin_classes_with_slides = [PageAdmin, GalleryAdmin, FlatPageAdmin]

for admin_class in admin_classes_with_slides:
    if hasattr(admin_class, 'inlines'):
        setattr(admin_class, 'inlines', list(admin_class.inlines) + [SlideInline])
    else:
        setattr(admin_class, 'inlines', [SlideInline,])
        
#admin.site.register(Slide, SlideAdmin)