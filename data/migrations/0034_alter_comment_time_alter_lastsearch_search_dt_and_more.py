# Generated by Django 4.2.3 on 2024-06-26 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0033_alter_comment_time_alter_lastsearch_search_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 26, 22, 43, 38, 477400)),
        ),
        migrations.AlterField(
            model_name='lastsearch',
            name='search_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 26, 22, 43, 38, 478400), null=True),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 26, 22, 43, 38, 477400)),
        ),
    ]
