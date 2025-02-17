from django.db import models


class ContactUs(models.Model):
    head_title = models.CharField(max_length=200, verbose_name='سر تیتر', null=True, blank=True)
    head_text = models.TextField(null=True, blank=True, verbose_name='متن سر تیتر')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.head_title

    class Meta:
        verbose_name = 'سرتیتر تماس با ما'
        verbose_name_plural = 'سرتیتر های تماس با ما'


# Create your models here.
class ContactUsBox(models.Model):
    class InputChoices(models.TextChoices):
        email = "email", "ایمیل"
        phone = "phone", "شماره تماس"
        location = "location", "موقعیت مکانی"

    kind = models.CharField(max_length=200, choices=InputChoices.choices, default=InputChoices.email,
                            verbose_name='نوع باکس')
    box_title = models.CharField(max_length=200, verbose_name='تیتر باکس', null=True, blank=True)
    box_text1 = models.TextField(null=True, blank=True, verbose_name='متن اول باکس')
    box_text2 = models.TextField(null=True, blank=True, verbose_name='متن دوم باکس')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return f'{self.box_title} / {self.kind}'

    class Meta:
        verbose_name = 'جعبه تماس با ما'
        verbose_name_plural = 'جعبه های تماس با ما'
