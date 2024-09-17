# Generated by Django 4.2.3 on 2024-06-30 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0044_remove_projectphoto_img1_remove_projectphoto_img2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='bootS',
        ),
        migrations.RemoveField(
            model_name='project',
            name='bostG',
        ),
        migrations.RemoveField(
            model_name='project',
            name='css',
        ),
        migrations.RemoveField(
            model_name='project',
            name='dj',
        ),
        migrations.RemoveField(
            model_name='project',
            name='html',
        ),
        migrations.RemoveField(
            model_name='project',
            name='js',
        ),
        migrations.RemoveField(
            model_name='project',
            name='py',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 0, 24, 50, 356218)),
        ),
        migrations.AlterField(
            model_name='lastsearch',
            name='search_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 1, 0, 24, 50, 358218), null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 0, 24, 50, 357218)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 0, 24, 50, 356218)),
        ),
    ]
