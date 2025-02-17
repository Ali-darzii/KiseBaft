from modeltranslation.translator import TranslationOptions, register
from .models import Slider, HomeBox


@register(Slider)
class ProductTranslationOptions(TranslationOptions):
    fields = ['title', 'text', 'box_title']


@register(HomeBox)
class ProductTranslationOptions(TranslationOptions):
    fields = ['title', 'text']
