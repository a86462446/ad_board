# Generated by Django 4.1.7 on 2023-06-03 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_video_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='file',
        ),
    ]
