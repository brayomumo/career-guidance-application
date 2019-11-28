# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-28 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allcourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_code', models.IntegerField()),
                ('university', models.CharField(max_length=200)),
                ('course_name', models.CharField(max_length=200)),
                ('cp', models.FloatField()),
                ('cutoffpoints_2014', models.FloatField()),
                ('cutoffpoints_2015_cp', models.FloatField()),
                ('cutoffpoints_2016_cp', models.FloatField()),
                ('cutoffpoints_2017_cp', models.FloatField()),
                ('cutoffpoints_2018_cp', models.FloatField()),
                ('course_id', models.IntegerField()),
            ],
        ),
    ]