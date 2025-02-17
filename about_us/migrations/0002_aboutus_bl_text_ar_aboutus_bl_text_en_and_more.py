# Generated by Django 4.2.6 on 2023-10-29 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='bl_text_ar',
            field=models.TextField(blank=True, null=True, verbose_name='متن باکس پایین چپ'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='bl_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='متن باکس پایین چپ'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='bl_text_fa',
            field=models.TextField(blank=True, null=True, verbose_name='متن باکس پایین چپ'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='br_text_ar',
            field=models.TextField(blank=True, null=True, verbose_name='متن پایین راست'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='br_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='متن پایین راست'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='br_text_fa',
            field=models.TextField(blank=True, null=True, verbose_name='متن پایین راست'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='footer_text_ar',
            field=models.TextField(blank=True, null=True, verbose_name='متن فووتر'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='footer_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='متن فووتر'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='footer_text_fa',
            field=models.TextField(blank=True, null=True, verbose_name='متن فووتر'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='footer_title_ar',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='سر تیتر فووتر'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='footer_title_en',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='سر تیتر فووتر'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='footer_title_fa',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='سر تیتر فووتر'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='head_title_ar',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='سر تیتر'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='head_title_en',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='سر تیتر'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='head_title_fa',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='سر تیتر'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tl_text_ar',
            field=models.TextField(blank=True, null=True, verbose_name='متن باکس بالا چپ'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tl_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='متن باکس بالا چپ'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tl_text_fa',
            field=models.TextField(blank=True, null=True, verbose_name='متن باکس بالا چپ'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tl_title_ar',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس بالا چپ'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tl_title_en',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس بالا چپ'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tl_title_fa',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس بالا چپ'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tr_text_ar',
            field=models.TextField(blank=True, null=True, verbose_name='متن باکس بالا راست'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tr_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='متن باکس بالا راست'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tr_text_fa',
            field=models.TextField(blank=True, null=True, verbose_name='متن باکس بالا راست'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tr_title_ar',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس بالا راست'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tr_title_en',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس بالا راست'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tr_title_fa',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس بالا راست'),
        ),
    ]
