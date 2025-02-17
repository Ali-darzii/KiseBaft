from modeltranslation.translator import TranslationOptions, register
from .models import AboutUs


@register(AboutUs)
class ProductTranslationOptions(TranslationOptions):
    fields = ['head_title', 'tr_title', 'tr_text', 'tl_title', 'tl_text', 'bl_text', 'br_text', 'footer_title',
              'footer_text']
