from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class StockBag(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام کیسه درجه 2', db_index=True)
    url_title = models.CharField(max_length=200, unique=True, verbose_name='نام در url', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'گونی ساده'
        verbose_name_plural = 'گونی های ساده'

    def __str__(self):
        return self.title


class SimpleBag(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام کیسه ساده', db_index=True)
    url_title = models.CharField(max_length=200, unique=True, verbose_name='نام در url', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'گونی ساده'
        verbose_name_plural = 'گونی های ساده'

    def __str__(self):
        return self.title


class ProductType(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام نوع محصول', db_index=True)
    url_title = models.CharField(max_length=200, unique=True, verbose_name='نام در url', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'نوع محصول'
        verbose_name_plural = 'نوع محصول ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('نام محصول'))
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    descriptions = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='نوع محصول', null=True,
                                     blank=True)
    simple_bag = models.ForeignKey(SimpleBag, on_delete=models.CASCADE, verbose_name='گونی ساده', null=True, blank=True)
    stock_bag = models.ForeignKey(StockBag, on_delete=models.CASCADE, verbose_name='گونی درجه 2', null=True, blank=True)
    inventory = models.BooleanField(verbose_name='موحودی', default=True)

    def get_absolute_url(self):
        return reverse('product_detail_page', args=[self.slug])

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "محصول"  #
        verbose_name_plural = "محصولات"


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='ای پی کابر')

    def __str__(self):
        return f"{self.product.title} / {self.ip}"

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدیدهای محصول'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/product-gallery', verbose_name='تصویر محصولات')

    def __str__(self):
        return f'{self.product.title}/{self.image}'

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'گالری تصاویر'
