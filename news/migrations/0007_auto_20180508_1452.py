# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20180508_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='articles/', upload_to='articles/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='newsletterrecipients',
            name='email',
            field=models.CharField(max_length=60),
        ),
    ]