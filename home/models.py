from django.db import models


# Create your models here.

class Slider(models.Model):
    title = models.TextField(verbose_name='تیتر اسلایدر', blank=True, null=True)
    image = models.ImageField(verbose_name='عکس',upload_to='uploads/sliders', blank=True, null=True)
    text = models.TextField(verbose_name='متن اسلایدر', blank=True, null=True)
    box_title = models.CharField(max_length=200,verbose_name='تیتر تمام باکس ها', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='غیر/فعال')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'


# class HomeBoxes(models.Model):
#     class ImageType(models.TextChoices):
#         email = "ooo.png", "ایمیل"
#         home = "shape-1.png", "خانه"
#         folder = "shape-5.png", "فولدر"
#         card = "shape-7.png", "کارت"
#
#     type = models.CharField(max_length=100, choices=ImageType.choices, verbose_name='نوع باکس')
#     title = models.TextField(verbose_name='تیتر')
#     text = models.TextField(verbose_name='متن')
#     url = models.CharField(max_length=200)
#     is_active = models.BooleanField(default=False, verbose_name='غیر/فعال')
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'باکس صفحه خانه'
#         verbose_name_plural = 'باکس های صفحه خانه'


# class HomeBoxes(models.Model):
#     title = models.TextField(verbose_name='تیتر')
#     text = models.TextField(verbose_name='متن')
#     url = models.CharField(max_length=200)
#     is_active = models.BooleanField(default=False, verbose_name='غیر/فعال')
#     image = models.ImageField(upload_to='uploads/boxes', verbose_name='تصویر')
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'باکس صفحه خانه'
#         verbose_name_plural = 'باکس های صفحه خانه'


class HomeBox(models.Model):
    title = models.TextField(verbose_name='تیتر')
    text = models.TextField(verbose_name='متن')
    url = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False, verbose_name='غیر/فعال')
    image = models.ImageField(upload_to='uploads/boxes', verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'باکس صفحه خانه'
        verbose_name_plural = 'باکس های صفحه خانه'