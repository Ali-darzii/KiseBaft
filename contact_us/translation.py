from modeltranslation.translator import TranslationOptions, register
from .models import ContactUsBox, ContactUs


@register(ContactUsBox)
class ProductTranslationOptions(TranslationOptions):
    fields = ['kind', 'box_title', 'box_text1', 'box_text2']


@register(ContactUs)
class ProductTranslationOptions(TranslationOptions):
    fields = ['head_title', 'head_text']
