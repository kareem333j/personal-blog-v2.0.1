# Generated by Django 4.2.3 on 2023-07-30 13:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_sociallinks_alter_comment_time_alter_usermsg_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='img3',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 30, 16, 14, 56, 124613)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 30, 16, 14, 56, 124613)),
        ),
        migrations.CreateModel(
            name='ProjectPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, default='default/product.png', null=True, upload_to='projects/%d')),
                ('img2', models.ImageField(blank=True, default='default/product.png', null=True, upload_to='projects/%d')),
                ('img3', models.ImageField(blank=True, default='default/product.png', null=True, upload_to='projects/%d')),
                ('project', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Project', to='data.project')),
            ],
        ),
    ]
