from modeltranslation.translator import translator, TranslationOptions
from mezzanine.core.translation import (TranslatedSlugged,)
from slides.models import Slide


class TranslatedSlide(TranslationOptions):
    fields = ('description', 'caption')

translator.register(Slide, TranslatedSlide)