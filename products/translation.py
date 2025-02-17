from modeltranslation.translator import TranslationOptions, register
from .models import Product, ProductType, StockBag, SimpleBag


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ['title', 'descriptions']


@register(ProductType)
class ProductTranslationOptions(TranslationOptions):
    fields = ['title']


@register(StockBag)
class ProductTranslationOptions(TranslationOptions):
    fields = ['title']


@register(SimpleBag)
class ProductTranslationOptions(TranslationOptions):
    fields = ['title']
