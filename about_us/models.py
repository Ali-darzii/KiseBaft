from django.db import models


# Create your models here.

class AboutUs(models.Model):
    head_title = models.TextField(max_length=200, verbose_name='سر تیتر', null=True, blank=True)
    # top right
    tr_title = models.TextField(max_length=200, verbose_name='تیتر باکس بالا راست', null=True, blank=True)
    tr_text = models.TextField(verbose_name='متن باکس بالا راست', null=True, blank=True)
    # top left
    tl_title = models.TextField(max_length=200, verbose_name='تیتر باکس بالا چپ', null=True, blank=True)
    tl_text = models.TextField(verbose_name='متن باکس بالا چپ', null=True, blank=True)
    # bottom left
    bl_text = models.TextField(verbose_name='متن باکس پایین چپ', null=True, blank=True)
    br_text = models.TextField(verbose_name='متن پایین راست', null=True, blank=True)
    # footer
    footer_title = models.TextField(max_length=200, verbose_name='سر تیتر فووتر', null=True, blank=True)
    footer_text = models.TextField(verbose_name='متن فووتر', null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')

    def __str__(self):
        return self.head_title

    class Meta:
        verbose_name = 'لیست درباره ما'
        verbose_name_plural = 'درباره ما'
