# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('comments_text', models.TextField()),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_article',
            field=models.ForeignKey(to='article.Article'),
        ),
    ]
