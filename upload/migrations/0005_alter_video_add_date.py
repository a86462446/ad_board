# Generated by Django 4.1.7 on 2023-06-03 02:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_remove_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='add_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
