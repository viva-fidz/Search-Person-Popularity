# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор ключевого слова')),
                ('Name', models.CharField(max_length=2048, verbose_name='Значение ключевого слова')),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор страницы')),
                ('Url', models.CharField(max_length=2048, verbose_name='Адрес страницы')),
                ('FoundDateTime', models.DateTimeField(blank=True, verbose_name='Дата и время обнаружения страницы системой')),
                ('lastScanDate', models.DateTimeField(blank=True, verbose_name='Дата и время последней проверки на упоминания')),
            ],
        ),
        migrations.CreateModel(
            name='Personpagerank',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('Rank', models.PositiveIntegerField(default=0, verbose_name='Количество упоминаний')),
                ('PageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spp.Pages')),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор личности')),
                ('name', models.CharField(max_length=2048, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор сайта')),
                ('Name', models.CharField(max_length=256, verbose_name='Наименование сайта')),
            ],
        ),
        migrations.AddField(
            model_name='personpagerank',
            name='PersonID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spp.Persons', verbose_name='Идентификатор личности'),
        ),
        migrations.AddField(
            model_name='pages',
            name='SiteID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spp.Sites'),
        ),
        migrations.AddField(
            model_name='keywords',
            name='PersonID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spp.Persons'),
        ),
    ]
