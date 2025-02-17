# Generated by Django 4.2.6 on 2023-10-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_descriptions_ar_product_descriptions_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=300, verbose_name='نام محصولل'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_ar',
            field=models.CharField(max_length=300, null=True, verbose_name='نام محصولل'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=300, null=True, verbose_name='نام محصولل'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_fa',
            field=models.CharField(max_length=300, null=True, verbose_name='نام محصولل'),
        ),
    ]
