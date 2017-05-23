# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_text', models.CharField(max_length=900)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_label', models.CharField(max_length=100)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Article')),
            ],
        ),
    ]
