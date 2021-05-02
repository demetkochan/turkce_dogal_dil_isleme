from django import forms
from .models import FileUpload



class UploadFileForm(forms.ModelForm):
    class Meta:
        model= FileUpload
        fields = ['file']