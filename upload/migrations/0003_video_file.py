# Generated by Django 4.1.7 on 2023-05-23 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_alter_video_videoname'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='file',
            field=models.FileField(default=123, upload_to='uploads_file/'),
            preserve_default=False,
        ),
    ]
