# Generated by Django 4.2.3 on 2024-06-26 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0030_alter_comment_time_alter_usermsg_time_lastsearch'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 26, 22, 39, 36, 654337)),
        ),
        migrations.AlterField(
            model_name='lastsearch',
            name='search_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 26, 22, 39, 36, 656841), null=True),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 26, 22, 39, 36, 655338)),
        ),
    ]
