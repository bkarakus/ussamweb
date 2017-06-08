from modeltranslation.translator import translator, TranslationOptions
from mezzanine.core.translation import (TranslatedSlugged,
                                        TranslatedDisplayable,
                                        TranslatedRichText)
from flatpages.models import FlatPageCategory, FlatPage, FlatPageIndex
from mezzanine.pages.translation import TranslatedPage


class TranslatedFlatPage(TranslatedDisplayable, TranslatedRichText):
    fields = ()

class TranslatedFlatPageCategory(TranslatedSlugged):
    fields = ()
    
class TranslatedFlatPageIndex(TranslationOptions):
    fields = ()

translator.register(FlatPage, TranslatedFlatPage)
translator.register(FlatPageCategory, TranslatedFlatPageCategory)

translator.register(FlatPageIndex, TranslatedFlatPageIndex)
