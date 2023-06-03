from datetime import date
from django.db import models

# Create your models here.

class Video(models.Model):
    # file= models.FileField(upload_to='uploads_file/')
    videoname= models.CharField(max_length=500)
    add_date= models.DateField(default= date.today)

    def __str__(self):
        return f"{self.videoname}"

