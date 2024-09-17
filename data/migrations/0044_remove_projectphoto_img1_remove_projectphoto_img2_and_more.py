# Generated by Django 4.2.3 on 2024-06-30 21:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0043_code_file_name_alter_comment_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectphoto',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='projectphoto',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='projectphoto',
            name='img3',
        ),
        migrations.AddField(
            model_name='projectphoto',
            name='img',
            field=models.ImageField(blank=True, default='default/project.png', null=True, upload_to='projects/images/%d'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 0, 1, 51, 234385)),
        ),
        migrations.AlterField(
            model_name='lastsearch',
            name='search_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 1, 0, 1, 51, 236386), null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 0, 1, 51, 235385)),
        ),
        migrations.AlterField(
            model_name='projectphoto',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Project', to='data.project'),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 0, 1, 51, 234385)),
        ),
        migrations.CreateModel(
            name='ProjectLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=100)),
                ('img', models.ImageField(blank=True, default='default/project.png', null=True, upload_to='projects/language/%d')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Language', to='data.project')),
            ],
        ),
    ]
