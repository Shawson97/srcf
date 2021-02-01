from django import forms
from .models import Upload, Comment

class UploadCreateForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('Title', 'Issn', 'description')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AddCreateForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('Title', 'Issn')
