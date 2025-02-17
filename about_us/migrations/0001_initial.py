# Generated by Django 4.2.6 on 2023-10-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_title', models.TextField(blank=True, max_length=200, null=True, verbose_name='سر تیتر')),
                ('tr_title', models.TextField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس بالا راست')),
                ('tr_text', models.TextField(blank=True, null=True, verbose_name='متن باکس بالا راست')),
                ('tl_title', models.TextField(blank=True, max_length=200, null=True, verbose_name='تیتر باکس بالا چپ')),
                ('tl_text', models.TextField(blank=True, null=True, verbose_name='متن باکس بالا چپ')),
                ('bl_text', models.TextField(blank=True, null=True, verbose_name='متن باکس پایین چپ')),
                ('br_text', models.TextField(blank=True, null=True, verbose_name='متن پایین راست')),
                ('footer_title', models.TextField(blank=True, max_length=200, null=True, verbose_name='سر تیتر فووتر')),
                ('footer_text', models.TextField(blank=True, null=True, verbose_name='متن فووتر')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیر فعال')),
            ],
            options={
                'verbose_name': 'لیست درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
    ]
