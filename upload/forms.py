from django import forms
from .models import Video
		
# Class for verify if the file is selected in function of upload_file
# 確認是否有選擇檔案
class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Video
        fields = {'videoname', 'add_date'}