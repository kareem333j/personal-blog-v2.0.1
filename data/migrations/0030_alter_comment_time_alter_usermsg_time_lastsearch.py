# Generated by Django 4.2.3 on 2024-06-25 12:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0029_statistics_alter_comment_time_alter_usermsg_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 15, 30, 15, 324798)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 15, 30, 15, 325798)),
        ),
        migrations.CreateModel(
            name='LastSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('search_dt', models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 25, 15, 30, 15, 326798), null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to='data.profile')),
            ],
        ),
    ]
