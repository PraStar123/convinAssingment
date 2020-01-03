from django import forms 
from .models import FileModel

class FileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ('fileName', 'filePath')
        

class FileUpdateForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ('fileName', 'filePath')
        