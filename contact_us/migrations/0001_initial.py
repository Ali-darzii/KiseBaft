# Generated by Django 4.2.6 on 2023-10-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='سر تیتر')),
                ('text1', models.TextField(blank=True, null=True, verbose_name='متن اول')),
                ('text2', models.TextField(blank=True, null=True, verbose_name='متن دوم')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
    ]
