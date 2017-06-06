from modeltranslation.translator import translator
from mezzanine.core.translation import (TranslatedSlugged,
                                        TranslatedDisplayable,
                                        TranslatedRichText)
from flatpages.models import FlatPageCategory, FlatPage


class TranslatedFlatPage(TranslatedDisplayable, TranslatedRichText):
    fields = ()


class TranslatedFlatPageCategory(TranslatedSlugged):
    fields = ()

translator.register(FlatPage, TranslatedFlatPage)
translator.register(FlatPageCategory, TranslatedFlatPageCategory)