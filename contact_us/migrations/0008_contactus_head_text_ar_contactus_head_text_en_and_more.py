# Generated by Django 4.2.6 on 2023-10-29 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0007_alter_contactusbox_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='head_text_ar',
            field=models.TextField(blank=True, null=True, verbose_name='متن سر تیتر'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='head_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='متن سر تیتر'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='head_text_fa',
            field=models.TextField(blank=True, null=True, verbose_name='متن سر تیتر'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='head_title_ar',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='سر تیتر'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='head_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='سر تیتر'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='head_title_fa',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='سر تیتر'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='box_text1_ar',
            field=models.TextField(blank=True, null=True, verbose_name='متن اول باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='box_text1_en',
            field=models.TextField(blank=True, null=True, verbose_name='متن اول باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='box_text1_fa',
            field=models.TextField(blank=True, null=True, verbose_name='متن اول باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='box_text2_ar',
            field=models.TextField(blank=True, null=True, verbose_name='متن دوم باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='box_text2_en',
            field=models.TextField(blank=True, null=True, verbose_name='متن دوم باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='box_text2_fa',
            field=models.TextField(blank=True, null=True, verbose_name='متن دوم باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='box_title_ar',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='box_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='box_title_fa',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='kind_ar',
            field=models.CharField(choices=[('email', 'ایمیل'), ('phone', 'شماره تماس'), ('location', 'موقعیت مکانی')], default='email', max_length=200, null=True, verbose_name='نوع باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='kind_en',
            field=models.CharField(choices=[('email', 'ایمیل'), ('phone', 'شماره تماس'), ('location', 'موقعیت مکانی')], default='email', max_length=200, null=True, verbose_name='نوع باکس'),
        ),
        migrations.AddField(
            model_name='contactusbox',
            name='kind_fa',
            field=models.CharField(choices=[('email', 'ایمیل'), ('phone', 'شماره تماس'), ('location', 'موقعیت مکانی')], default='email', max_length=200, null=True, verbose_name='نوع باکس'),
        ),
    ]
