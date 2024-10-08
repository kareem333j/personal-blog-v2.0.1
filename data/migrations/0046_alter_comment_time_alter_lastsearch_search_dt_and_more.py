# Generated by Django 4.2.3 on 2024-07-01 15:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0045_remove_project_boots_remove_project_bostg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 18, 2, 39, 998043)),
        ),
        migrations.AlterField(
            model_name='lastsearch',
            name='search_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 1, 18, 2, 40, 5388), null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 18, 2, 40, 3455)),
        ),
        migrations.AlterField(
            model_name='projectphoto',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProjectPhoto', to='data.project'),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 18, 2, 40, 2455)),
        ),
    ]
