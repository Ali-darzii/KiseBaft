from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.ProductVisit)
admin.site.register(models.ProductGallery)
admin.site.register(models.SimpleBag)
admin.site.register(models.StockBag)
admin.site.register(models.ProductType)

