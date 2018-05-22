# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('pic', models.ImageField(upload_to=b'uploads', verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9b\xbe')),
                ('adurl', models.URLField(verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
                ('adlocation', models.CharField(max_length=2, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae')),
                ('status', models.CharField(default=1, max_length=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('slug', models.SlugField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', unique_for_year=b'publish_date')),
                ('content', DjangoUeditor.models.UEditorField(default=b'', verbose_name='\u5185\u5bb9', blank=True)),
                ('status', models.CharField(max_length=2, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2018, 5, 20, 21, 6, 45, 799000), verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f')),
                ('expiration_date', models.DateTimeField(null=True, verbose_name=b'\xe6\x9c\x89\xe6\x95\x88\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\x83\xad\xe9\x97\xa8')),
                ('pic', models.ImageField(upload_to=b'uploads', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('author', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u65b0\u95fb\u6587\u7ae0',
                'verbose_name_plural': '\u65b0\u95fb\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u65b0\u95fb\u7c7b\u522b',
                'verbose_name_plural': '\u65b0\u95fb\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('completed', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xae\x8c\xe6\x88\x90')),
                ('article_category', models.ForeignKey(to='article.Category')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u65b0\u95fb\u5b50\u680f\u76ee',
                'verbose_name_plural': '\u65b0\u95fb\u5b50\u680f\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('slug', models.SlugField(verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='item',
            field=models.ForeignKey(verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe5\x90\x8d\xe7\xa7\xb0', to='article.Item'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='article.Tag', blank=True),
        ),
    ]
